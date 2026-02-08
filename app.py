from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from resume_parser.extract_text import extract_text_from_pdf
from resume_parser.skill_extractor import extract_skills
from resume_parser.clean_text import clean_text
from resume_parser.entity_extractor import extract_entities
from ats_score.ats_calculator import calculate_ats_score
from ats_score.suggestions import generate_suggestions
from job_matcher.matcher import find_matching_jobs
from job_matcher.ranker import rank_jobs

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'docx', 'txt'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    try:
        # Check if file is present
        if 'resume' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['resume']
        job_description = request.form.get('job_description', '')
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Please upload PDF, DOCX, or TXT'}), 400
        
        # Save file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Extract and process resume text
        resume_text = extract_text_from_pdf(filepath)
        cleaned_resume = clean_text(resume_text)
        
        # Extract skills
        resume_skills = extract_skills(cleaned_resume)
        
        # Extract entities (name, email, phone, etc.)
        entities = extract_entities(resume_text)
        
        # Calculate ATS score
        ats_score = calculate_ats_score(cleaned_resume, job_description)
        
        # Generate suggestions
        suggestions = generate_suggestions(cleaned_resume, job_description, ats_score)
        
        # Find matching jobs
        matching_jobs = find_matching_jobs(resume_skills, resume_text)
        ranked_jobs = rank_jobs(matching_jobs, resume_skills)
        
        # Clean up uploaded file
        os.remove(filepath)
        
        return jsonify({
            'success': True,
            'ats_score': ats_score,
            'skills': resume_skills,
            'entities': entities,
            'suggestions': suggestions,
            'matching_jobs': ranked_jobs[:5]  # Top 5 jobs
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
