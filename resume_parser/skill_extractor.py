import os
import re

# Common technical skills database
COMMON_SKILLS = [
    'python', 'java', 'javascript', 'c++', 'c#', 'ruby', 'php', 'swift', 'kotlin',
    'react', 'angular', 'vue', 'node.js', 'django', 'flask', 'spring', 'express',
    'html', 'css', 'sql', 'nosql', 'mongodb', 'postgresql', 'mysql', 'redis',
    'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins', 'git', 'ci/cd',
    'machine learning', 'deep learning', 'tensorflow', 'pytorch', 'scikit-learn',
    'data analysis', 'data visualization', 'pandas', 'numpy', 'matplotlib',
    'agile', 'scrum', 'jira', 'rest api', 'graphql', 'microservices',
    'linux', 'unix', 'windows', 'bash', 'powershell',
    'communication', 'leadership', 'problem solving', 'teamwork', 'project management'
]

def extract_skills(text):
    """Extract skills from resume text"""
    if not text:
        return []
    
    text_lower = text.lower()
    found_skills = []
    
    # Load skills from file if exists
    skills_file = os.path.join('data', 'skills_list.txt')
    skills_to_check = COMMON_SKILLS.copy()
    
    if os.path.exists(skills_file):
        try:
            with open(skills_file, 'r') as f:
                file_skills = [line.strip().lower() for line in f if line.strip()]
                skills_to_check.extend(file_skills)
        except:
            pass
    
    # Remove duplicates
    skills_to_check = list(set(skills_to_check))
    
    # Find skills in text
    for skill in skills_to_check:
        # Use word boundary to match whole words
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill.title())
    
    return sorted(list(set(found_skills)))
