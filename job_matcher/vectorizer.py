from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def vectorize_text(texts):
    """Vectorize text using TF-IDF"""
    vectorizer = TfidfVectorizer(
        max_features=200,
        stop_words='english',
        ngram_range=(1, 2),  # Include bigrams
        min_df=1,
        max_df=0.9
    )
    
    try:
        vectors = vectorizer.fit_transform(texts)
        return vectors, vectorizer
    except Exception as e:
        print(f"Vectorization error: {e}")
        return None, None

def calculate_similarity(resume_vector, job_vectors):
    """Calculate cosine similarity between resume and jobs"""
    try:
        similarities = cosine_similarity(resume_vector, job_vectors)
        return similarities[0]
    except:
        return np.array([])

def get_skill_similarity(resume_skills, job_skills):
    """Calculate Jaccard similarity between skill sets"""
    resume_set = set([s.lower().strip() for s in resume_skills])
    job_set = set([s.lower().strip() for s in job_skills])
    
    if not job_set:
        return 0.0
    
    intersection = len(resume_set.intersection(job_set))
    union = len(resume_set.union(job_set))
    
    return (intersection / union * 100) if union > 0 else 0.0
