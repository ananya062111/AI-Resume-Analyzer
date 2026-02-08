import os
import csv
from .vectorizer import get_skill_similarity

def find_matching_jobs(resume_skills, resume_text=''):
    """Find matching jobs based on resume skills using ML algorithms"""
    matching_jobs = []
    
    # Path to job descriptions CSV
    csv_path = os.path.join('data', 'job_descriptions.csv')
    
    if not os.path.exists(csv_path):
        # Return sample jobs if CSV doesn't exist
        return get_sample_jobs()
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                job_title = row.get('title', '')
                job_skills = row.get('skills', '').lower().split(',')
                job_skills = [skill.strip() for skill in job_skills if skill.strip()]
                
                # Convert resume skills to lowercase for comparison
                resume_skills_lower = [skill.lower().strip() for skill in resume_skills]
                
                # Calculate skill match using exact matching
                matched_skills = set(resume_skills_lower).intersection(set(job_skills))
                exact_match = (len(matched_skills) / len(job_skills) * 100) if job_skills else 0
                
                # Calculate Jaccard similarity for a more nuanced score
                similarity_score = get_skill_similarity(resume_skills_lower, job_skills)
                
                # Weighted average: 60% exact match, 40% similarity
                final_match = (exact_match * 0.6) + (similarity_score * 0.4)
                
                if final_match > 0:
                    matching_jobs.append({
                        'title': job_title,
                        'company': row.get('company', 'N/A'),
                        'location': row.get('location', 'N/A'),
                        'required_skills': job_skills,
                        'matched_skills': list(matched_skills),
                        'match_percentage': round(final_match, 2),
                        'description': row.get('description', '')
                    })
    
    except Exception as e:
        print(f"Error reading job descriptions: {e}")
        return get_sample_jobs()
    
    return matching_jobs if matching_jobs else get_sample_jobs()

def get_sample_jobs():
    """Return sample jobs when CSV is not available"""
    return [
        {
            'title': 'Software Engineer',
            'company': 'Tech Corp',
            'location': 'San Francisco, CA',
            'required_skills': ['python', 'javascript', 'react'],
            'matched_skills': ['python'],
            'match_percentage': 33.33
        },
        {
            'title': 'Data Scientist',
            'company': 'Data Inc',
            'location': 'New York, NY',
            'required_skills': ['python', 'machine learning', 'sql'],
            'matched_skills': ['python'],
            'match_percentage': 33.33
        },
        {
            'title': 'Full Stack Developer',
            'company': 'Web Solutions',
            'location': 'Remote',
            'required_skills': ['javascript', 'node.js', 'react', 'mongodb'],
            'matched_skills': ['javascript'],
            'match_percentage': 25.0
        }
    ]
