import re

def clean_text(text):
    """Clean and normalize text"""
    if not text:
        return ""
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove special characters but keep alphanumeric and basic punctuation
    text = re.sub(r'[^\w\s\.,;:()\-]', '', text)
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # Remove email addresses (optional - might want to keep)
    # text = re.sub(r'\S+@\S+', '', text)
    
    # Normalize case
    text = text.lower()
    
    return text.strip()
