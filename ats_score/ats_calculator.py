import re
from difflib import SequenceMatcher

def calculate_ats_score(resume_text, job_description):
    """Calculate ATS (Applicant Tracking System) score"""
    if not resume_text or not job_description:
        return 0
    
    resume_lower = resume_text.lower()
    jd_lower = job_description.lower()
    
    # Extract keywords from job description (words longer than 3 chars)
    jd_words = set(re.findall(r'\b\w{4,}\b', jd_lower))
    resume_words = set(re.findall(r'\b\w{4,}\b', resume_lower))
    
    # Remove common stop words
    stop_words = {'that', 'this', 'with', 'from', 'have', 'will', 'your', 
                  'about', 'which', 'their', 'would', 'there', 'could', 'been'}
    jd_words -= stop_words
    resume_words -= stop_words
    
    if not jd_words:
        return 0
    
    # Calculate keyword match percentage
    matched_keywords = jd_words.intersection(resume_words)
    keyword_match_score = (len(matched_keywords) / len(jd_words)) * 100
    
    # Calculate text similarity using SequenceMatcher
    similarity_score = SequenceMatcher(None, resume_lower, jd_lower).ratio() * 100
    
    # Weighted average (70% keywords, 30% similarity)
    final_score = (keyword_match_score * 0.7) + (similarity_score * 0.3)
    
    return round(min(final_score, 100), 2)
