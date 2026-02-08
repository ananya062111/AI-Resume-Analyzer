import re

def generate_suggestions(resume_text, job_description, ats_score):
    """Generate suggestions to improve resume"""
    suggestions = []
    
    resume_lower = resume_text.lower()
    jd_lower = job_description.lower()
    
    # Extract keywords from job description
    jd_words = set(re.findall(r'\b\w{4,}\b', jd_lower))
    resume_words = set(re.findall(r'\b\w{4,}\b', resume_lower))
    
    # Remove common stop words
    stop_words = {'that', 'this', 'with', 'from', 'have', 'will', 'your', 
                  'about', 'which', 'their', 'would', 'there', 'could', 'been',
                  'more', 'some', 'than', 'into', 'very', 'also', 'just'}
    jd_words -= stop_words
    
    # Find missing keywords
    missing_keywords = jd_words - resume_words
    
    # Categorize suggestions based on score
    if ats_score < 40:
        suggestions.append({
            'type': 'critical',
            'title': 'Low ATS Score',
            'description': 'Your resume needs significant improvements to match the job description.'
        })
    elif ats_score < 70:
        suggestions.append({
            'type': 'warning',
            'title': 'Moderate ATS Score',
            'description': 'Your resume partially matches the job description but could be improved.'
        })
    else:
        suggestions.append({
            'type': 'success',
            'title': 'Good ATS Score',
            'description': 'Your resume matches well with the job description!'
        })
    
    # Keyword suggestions
    if missing_keywords:
        top_missing = list(missing_keywords)[:10]
        suggestions.append({
            'type': 'info',
            'title': 'Missing Keywords',
            'description': f'Consider adding these keywords if relevant: {", ".join(top_missing)}'
        })
    
    # General suggestions
    if len(resume_text) < 500:
        suggestions.append({
            'type': 'warning',
            'title': 'Resume Length',
            'description': 'Your resume seems too short. Consider adding more details about your experience.'
        })
    
    # Check for common sections
    sections_to_check = ['experience', 'education', 'skills', 'projects']
    missing_sections = [section for section in sections_to_check if section not in resume_lower]
    
    if missing_sections:
        suggestions.append({
            'type': 'info',
            'title': 'Resume Structure',
            'description': f'Consider adding these sections: {", ".join(missing_sections)}'
        })
    
    return suggestions
