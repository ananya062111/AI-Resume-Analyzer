import re
from datetime import datetime

def extract_email(text):
    """Extract email address from text"""
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails[0] if emails else None

def extract_phone(text):
    """Extract phone number from text"""
    # Match various phone formats
    phone_patterns = [
        r'\+?1?\s*\(?(\d{3})\)?[\s.-]?(\d{3})[\s.-]?(\d{4})',  # US format
        r'\+?\d{1,3}[\s.-]?\(?\d{2,4}\)?[\s.-]?\d{3,4}[\s.-]?\d{3,4}',  # International
    ]
    
    for pattern in phone_patterns:
        phones = re.findall(pattern, text)
        if phones:
            if isinstance(phones[0], tuple):
                return f"({phones[0][0]}) {phones[0][1]}-{phones[0][2]}"
            return phones[0]
    
    return None

def extract_name(text):
    """Extract name from resume (heuristic approach)"""
    # Split into lines and look at first few lines
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    if not lines:
        return None
    
    # Name is usually in first 3 lines
    for line in lines[:3]:
        # Skip lines with email or phone
        if '@' in line or any(char.isdigit() for char in line) and len(line) < 50:
            continue
        
        # Check if line looks like a name (2-4 words, mostly letters)
        words = line.split()
        if 2 <= len(words) <= 4:
            if all(word[0].isupper() and word.isalpha() for word in words if word):
                return line
    
    return None

def extract_urls(text):
    """Extract URLs from text"""
    url_pattern = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)'
    urls = re.findall(url_pattern, text)
    return urls

def extract_linkedin(text):
    """Extract LinkedIn profile URL"""
    urls = extract_urls(text)
    linkedin = [url for url in urls if 'linkedin.com' in url.lower()]
    return linkedin[0] if linkedin else None

def extract_github(text):
    """Extract GitHub profile URL"""
    urls = extract_urls(text)
    github = [url for url in urls if 'github.com' in url.lower()]
    return github[0] if github else None

def extract_years_of_experience(text):
    """Estimate years of experience from text"""
    # Look for patterns like "5 years", "5+ years", etc.
    patterns = [
        r'(\d+)\+?\s*years?\s+(?:of\s+)?experience',
        r'experience[:\s]+(\d+)\+?\s*years?',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text.lower())
        if matches:
            return int(matches[0])
    
    # Try to extract from dates in experience section
    year_pattern = r'\b(19|20)\d{2}\b'
    years = [int(year) for year in re.findall(year_pattern, text)]
    
    if len(years) >= 2:
        min_year = min(years)
        max_year = max(years)
        current_year = datetime.now().year
        
        # If most recent year is close to current, estimate experience
        if abs(max_year - current_year) <= 2:
            return max_year - min_year
    
    return None

def extract_education(text):
    """Extract education information"""
    education = []
    
    # Common degree patterns
    degrees = [
        r'\b(?:Bachelor|B\.?S\.?|B\.?A\.?|B\.?Tech|B\.?E\.?)\b',
        r'\b(?:Master|M\.?S\.?|M\.?A\.?|M\.?Tech|M\.?E\.?|MBA)\b',
        r'\b(?:Ph\.?D\.?|Doctorate)\b',
        r'\b(?:Associate|A\.?S\.?|A\.?A\.?)\b',
    ]
    
    for degree_pattern in degrees:
        matches = re.finditer(degree_pattern, text, re.IGNORECASE)
        for match in matches:
            # Get surrounding context (50 chars before and after)
            start = max(0, match.start() - 50)
            end = min(len(text), match.end() + 50)
            context = text[start:end].strip()
            education.append(context)
    
    return education[:3]  # Return up to 3 education entries

def extract_certifications(text):
    """Extract certifications from text"""
    cert_keywords = [
        'certified', 'certification', 'certificate',
        'aws certified', 'microsoft certified', 'google certified',
        'cissp', 'pmp', 'scrum master', 'itil',
        'comptia', 'ccna', 'ccnp', 'ceh'
    ]
    
    certifications = []
    text_lower = text.lower()
    
    for keyword in cert_keywords:
        if keyword in text_lower:
            # Find the line containing this certification
            lines = text.split('\n')
            for line in lines:
                if keyword in line.lower():
                    certifications.append(line.strip())
                    break
    
    return list(set(certifications))[:5]  # Return up to 5 unique certifications

def extract_entities(text):
    """Extract all entities from resume text"""
    return {
        'name': extract_name(text),
        'email': extract_email(text),
        'phone': extract_phone(text),
        'linkedin': extract_linkedin(text),
        'github': extract_github(text),
        'experience_years': extract_years_of_experience(text),
        'education': extract_education(text),
        'certifications': extract_certifications(text)
    }
