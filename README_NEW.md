# 🎯 AI-Based Resume Analyzer & Job Matching System

An intelligent platform that analyzes resumes using **Natural Language Processing (NLP)** and **Machine Learning** to match candidates with the most relevant job roles. It evaluates skills, experience, keywords, and ATS compatibility to improve hiring accuracy and job seeker success.

## ✨ Features

### 1. **Resume Analysis**
- Extract text from PDF, DOCX, and TXT files
- Clean and normalize resume text
- Extract technical and soft skills (200+ skills in database)
- Entity extraction: name, email, phone, LinkedIn, GitHub, years of experience

### 2. **ATS Score Calculation**
- Keyword matching with job descriptions
- Text similarity analysis using NLP
- Weighted scoring algorithm (70% keywords + 30% similarity)
- Comprehensive improvement suggestions

### 3. **Intelligent Job Matching**
- Machine Learning-based job matching using TF-IDF vectorization
- Cosine similarity for semantic matching
- Jaccard similarity for skill set comparison
- Composite scoring algorithm for accurate ranking

### 4. **Advanced NLP Features**
- Contact information extraction (email, phone, social profiles)
- Education and certification detection
- Years of experience estimation
- Resume structure analysis

### 5. **Interactive Web Interface**
- Modern, responsive UI with gradient design
- Real-time analysis with loading animations
- Detailed results visualization
- Top 5 job recommendations

## 🛠️ Technologies Used

- **Backend**: Python 3.13, Flask
- **NLP/ML**: scikit-learn, NLTK
- **Document Processing**: PyPDF2, python-docx
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Algorithms**: TF-IDF, Cosine Similarity, Jaccard Similarity

## 📁 Project Structure

```
AI-Resume_Analyzer/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── resume_parser/              # Resume parsing modules
│   ├── extract_text.py        # Text extraction from files
│   ├── clean_text.py          # Text cleaning and normalization
│   ├── skill_extractor.py     # Skill detection
│   └── entity_extractor.py    # Contact info & entity extraction
│
├── ats_score/                  # ATS scoring modules
│   ├── ats_calculator.py      # ATS score calculation
│   └── suggestions.py         # Improvement suggestions
│
├── job_matcher/                # Job matching modules
│   ├── matcher.py             # Job matching algorithm
│   ├── ranker.py              # Job ranking algorithm
│   └── vectorizer.py          # ML vectorization & similarity
│
├── data/                       # Data files
│   ├── skills_list.txt        # 140+ skills database
│   └── job_descriptions.csv   # Sample job listings
│
├── templates/                  # HTML templates
│   ├── index.html             # Main page
│   └── result.html            # Results page
│
├── static/                     # Static assets
│   ├── style.css              # Stylesheet
│   └── script.js              # JavaScript logic
│
└── uploads/                    # Temporary file uploads
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Navigate to Project Directory
```bash
cd AI-Resume_Analyzer
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv .venv
```

### Step 3: Activate Virtual Environment
**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run the Application
```bash
python app.py
```

### Step 6: Access the Application
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## 📊 How It Works

### 1. **Upload Resume**
Users upload their resume in PDF, DOCX, or TXT format.

### 2. **Text Extraction**
The system extracts raw text from the document using PyPDF2 and python-docx.

### 3. **NLP Processing**
- Text cleaning and normalization
- Skill extraction using pattern matching
- Entity extraction (name, email, phone, links)
- Years of experience estimation

### 4. **ATS Scoring**
- Extract keywords from job description
- Calculate keyword match percentage
- Compute text similarity using SequenceMatcher
- Generate weighted ATS score

### 5. **Job Matching (ML Algorithm)**
```
For each job in database:
  1. Extract job skills and requirements
  2. Calculate exact skill match percentage
  3. Calculate Jaccard similarity (union/intersection)
  4. Compute TF-IDF vectors
  5. Calculate cosine similarity
  6. Generate composite score:
     Score = (ExactMatch × 0.6) + (Jaccard × 0.4)
```

### 6. **Job Ranking**
Jobs are ranked using a composite algorithm:
```
CompositeScore = (MatchPct × 0.7) + 
                 (MatchedCount × 10 × 0.2) + 
                 (Coverage × 0.1)
```

### 7. **Results Display**
- ATS score with visual indicator
- Extracted skills as badges
- Contact information card
- Personalized suggestions
- Top 5 matching jobs

## 🎯 ML Algorithms Explained

### TF-IDF (Term Frequency-Inverse Document Frequency)
Converts text into numerical vectors representing importance of words:
```python
TF-IDF = TF(word) × IDF(word)
TF = (word count) / (total words)
IDF = log(total docs / docs containing word)
```

### Cosine Similarity
Measures similarity between two vectors:
```python
similarity = (A · B) / (||A|| × ||B||)
```

### Jaccard Similarity
Measures similarity between skill sets:
```python
J(A, B) = |A ∩ B| / |A ∪ B|
```

## 📈 ATS Score Interpretation

| Score Range | Interpretation | Recommendation |
|-------------|----------------|----------------|
| 70-100% | Excellent Match | Apply with confidence |
| 40-69% | Good Match | Minor improvements needed |
| 0-39% | Poor Match | Significant improvements required |

## 🔧 Customization

### Adding More Skills
Edit `data/skills_list.txt` and add one skill per line:
```
blockchain
solidity
rust
go
```

### Adding More Jobs
Edit `data/job_descriptions.csv`:
```csv
title,company,location,skills,description
AI Engineer,Tech Co,Remote,python,tensorflow,nlp,Build AI models
```

### Modifying Scoring Weights
Edit `ats_score/ats_calculator.py`:
```python
final_score = (keyword_match_score * 0.7) + (similarity_score * 0.3)
```

## 🐛 Troubleshooting

### Issue: Module not found
**Solution:** Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: File upload fails
**Solution:** Check file size (max 16MB) and format (PDF, DOCX, TXT only)

### Issue: No skills detected
**Solution:** Ensure resume contains recognizable skills from the database

## 🚀 Future Enhancements

- [ ] Deep Learning models for resume parsing
- [ ] Multi-language support
- [ ] Resume template suggestions
- [ ] Salary prediction based on skills
- [ ] Integration with job boards APIs
- [ ] Resume comparison tool
- [ ] Export reports as PDF
- [ ] User authentication and history
- [ ] Real-time job alerts
- [ ] Interview question suggestions

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

Built with ❤️ for improving the job search experience

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Note:** This is a development server. For production deployment, use a WSGI server like Gunicorn or uWSGI.
