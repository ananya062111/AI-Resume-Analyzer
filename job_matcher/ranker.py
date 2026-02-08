def rank_jobs(jobs, resume_skills):
    """Rank jobs based on match percentage and other factors"""
    if not jobs:
        return []
    
    # Calculate a composite score for each job
    for job in jobs:
        match_pct = job.get('match_percentage', 0)
        matched_count = len(job.get('matched_skills', []))
        required_count = len(job.get('required_skills', []))
        
        # Composite score: 70% match percentage, 20% matched skills count, 10% coverage
        coverage = (matched_count / required_count * 100) if required_count > 0 else 0
        composite_score = (
            match_pct * 0.7 +
            min(matched_count * 10, 100) * 0.2 +
            coverage * 0.1
        )
        
        job['composite_score'] = round(composite_score, 2)
    
    # Sort jobs by composite score in descending order
    ranked_jobs = sorted(jobs, key=lambda x: x.get('composite_score', 0), reverse=True)
    
    return ranked_jobs
