document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('resumeForm');
    const fileInput = document.getElementById('resume');
    const fileName = document.querySelector('.file-name');
    const resultsSection = document.getElementById('results');
    const errorDiv = document.getElementById('error');
    
    // Update file name display
    if (fileInput && fileName) {
        fileInput.addEventListener('change', function() {
            if (this.files.length > 0) {
                fileName.textContent = this.files[0].name;
            } else {
                fileName.textContent = 'No file chosen';
            }
        });
    }
    
    // Handle form submission
    if (form) {
        form.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            // Show loading state
            const submitBtn = form.querySelector('button[type="submit"]');
            const btnText = submitBtn.querySelector('.btn-text');
            const loader = submitBtn.querySelector('.loader');
            
            btnText.style.display = 'none';
            loader.style.display = 'block';
            submitBtn.disabled = true;
            
            // Hide previous results and errors
            resultsSection.style.display = 'none';
            errorDiv.style.display = 'none';
            
            // Prepare form data
            const formData = new FormData(form);
            
            try {
                const response = await fetch('/analyze', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                
                if (data.success) {
                    // Display results
                    displayResults(data);
                    resultsSection.style.display = 'block';
                    
                    // Scroll to results
                    resultsSection.scrollIntoView({ behavior: 'smooth' });
                } else {
                    throw new Error(data.error || 'Analysis failed');
                }
                
            } catch (error) {
                errorDiv.textContent = 'Error: ' + error.message;
                errorDiv.style.display = 'block';
            } finally {
                // Reset button state
                btnText.style.display = 'inline';
                loader.style.display = 'none';
                submitBtn.disabled = false;
            }
        });
    }
    
    function displayResults(data) {
        // Display ATS Score
        const atsScoreElement = document.getElementById('atsScore');
        const scoreDescription = document.getElementById('scoreDescription');
        
        if (atsScoreElement) {
            atsScoreElement.textContent = data.ats_score;
            
            // Animate score
            animateScore(atsScoreElement, data.ats_score);
            
            // Set score description
            if (scoreDescription) {
                if (data.ats_score >= 70) {
                    scoreDescription.textContent = 'Excellent! Your resume matches well.';
                    scoreDescription.style.color = '#00b894';
                } else if (data.ats_score >= 40) {
                    scoreDescription.textContent = 'Good! Some improvements recommended.';
                    scoreDescription.style.color = '#fdcb6e';
                } else {
                    scoreDescription.textContent = 'Needs improvement. Follow suggestions below.';
                    scoreDescription.style.color = '#d63031';
                }
            }
        }
        
        // Display Skills
        const skillsList = document.getElementById('skillsList');
        if (skillsList && data.skills) {
            skillsList.innerHTML = '';
            if (data.skills.length === 0) {
                skillsList.innerHTML = '<p>No skills detected. Try uploading a more detailed resume.</p>';
            } else {
                data.skills.forEach(skill => {
                    const badge = document.createElement('span');
                    badge.className = 'skill-badge';
                    badge.textContent = skill;
                    skillsList.appendChild(badge);
                });
            }
        }
        
        // Display Entity Information
        const entityInfo = document.getElementById('entityInfo');
        if (entityInfo && data.entities) {
            entityInfo.innerHTML = '';
            
            const entities = data.entities;
            const displayEntities = [
                { label: 'Name', value: entities.name, type: 'text' },
                { label: 'Email', value: entities.email, type: 'email' },
                { label: 'Phone', value: entities.phone, type: 'text' },
                { label: 'LinkedIn', value: entities.linkedin, type: 'link' },
                { label: 'GitHub', value: entities.github, type: 'link' },
                { label: 'Experience', value: entities.experience_years ? `${entities.experience_years} years` : null, type: 'text' }
            ];
            
            displayEntities.forEach(entity => {
                if (entity.value) {
                    const item = document.createElement('div');
                    item.className = 'entity-item';
                    
                    const label = document.createElement('div');
                    label.className = 'entity-label';
                    label.textContent = entity.label;
                    
                    const value = document.createElement('div');
                    value.className = 'entity-value';
                    
                    if (entity.type === 'link') {
                        const link = document.createElement('a');
                        link.href = entity.value;
                        link.target = '_blank';
                        link.textContent = entity.value;
                        value.appendChild(link);
                    } else if (entity.type === 'email') {
                        const link = document.createElement('a');
                        link.href = `mailto:${entity.value}`;
                        link.textContent = entity.value;
                        value.appendChild(link);
                    } else {
                        value.textContent = entity.value;
                    }
                    
                    item.appendChild(label);
                    item.appendChild(value);
                    entityInfo.appendChild(item);
                }
            });
            
            if (entityInfo.children.length === 0) {
                entityInfo.innerHTML = '<p>No contact information detected.</p>';
            }
        }
        
        // Display Suggestions
        const suggestionsList = document.getElementById('suggestionsList');
        if (suggestionsList && data.suggestions) {
            suggestionsList.innerHTML = '';
            data.suggestions.forEach(suggestion => {
                const item = document.createElement('div');
                item.className = `suggestion-item ${suggestion.type}`;
                item.innerHTML = `
                    <div class="suggestion-title">${suggestion.title}</div>
                    <div class="suggestion-description">${suggestion.description}</div>
                `;
                suggestionsList.appendChild(item);
            });
        }
        
        // Display Matching Jobs
        const jobsList = document.getElementById('jobsList');
        if (jobsList && data.matching_jobs) {
            jobsList.innerHTML = '';
            if (data.matching_jobs.length === 0) {
                jobsList.innerHTML = '<p>No matching jobs found at the moment.</p>';
            } else {
                data.matching_jobs.forEach(job => {
                    const card = document.createElement('div');
                    card.className = 'job-card';
                    card.innerHTML = `
                        <div class="job-title">${job.title}</div>
                        <div class="job-info">📍 ${job.location}</div>
                        <div class="job-info">🏢 ${job.company}</div>
                        <div class="match-badge">Match: ${job.match_percentage}%</div>
                    `;
                    jobsList.appendChild(card);
                });
            }
        }
    }
    
    function animateScore(element, targetScore) {
        let currentScore = 0;
        const increment = targetScore / 50;
        const timer = setInterval(() => {
            currentScore += increment;
            if (currentScore >= targetScore) {
                currentScore = targetScore;
                clearInterval(timer);
            }
            element.textContent = Math.round(currentScore);
        }, 20);
    }
});
