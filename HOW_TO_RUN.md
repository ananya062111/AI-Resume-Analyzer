# 🚀 How to Run This Project Successfully

## ✅ Current Status
**Your application is RUNNING at: http://127.0.0.1:5000**

---

## 📋 Quick Start (3 Steps)

### Step 1: Open Terminal
Open PowerShell or Command Prompt in the project directory

### Step 2: Activate Virtual Environment
```bash
.venv\Scripts\activate
```

### Step 3: Run the Application
```bash
python app.py
```

**That's it!** Open http://127.0.0.1:5000 in your browser.

---

## 🔧 Complete Setup Guide (First Time Only)

### Prerequisites
- ✅ Python 3.8 or higher installed
- ✅ pip (comes with Python)

### Step-by-Step Installation

#### 1. Navigate to Project Directory
```bash
cd C:\Users\baner\OneDrive\Desktop\AI-Resume_Analyzer
```

#### 2. Create Virtual Environment (First Time Only)
```bash
python -m venv .venv
```

#### 3. Activate Virtual Environment
**Windows PowerShell:**
```bash
.venv\Scripts\activate
```

**Windows CMD:**
```bash
.venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

You'll see `(.venv)` appear in your terminal prompt.

#### 4. Install Dependencies (First Time Only)
```bash
pip install -r requirements.txt
```

This installs:
- Flask (web framework)
- PyPDF2 (PDF processing)
- python-docx (Word processing)
- scikit-learn (Machine Learning)
- nltk (Natural Language Processing)
- And other required packages

#### 5. Run the Application
```bash
python app.py
```

#### 6. Access the Application
Open your browser and go to:
```
http://127.0.0.1:5000
```
or
```
http://localhost:5000
```

---

## 🎯 Usage Instructions

### 1. Upload Resume
- Click "Choose File" button
- Select a PDF, DOCX, or TXT file
- Maximum size: 16MB

### 2. Add Job Description (Optional)
- Paste job description in the text area
- This gives you a personalized ATS score
- Leave blank for general analysis

### 3. Click "Analyze Resume"
- Wait 1-2 seconds for processing
- View your results!

### 4. View Results
You'll see:
- **ATS Score** (0-100%)
- **Contact Information** (name, email, phone, LinkedIn, GitHub)
- **Extracted Skills** (displayed as badges)
- **Suggestions** for improvement
- **Top 5 Matching Jobs** from database

---

## 🧪 Testing the Application

### Test with Sample Resume
Use the provided `sample_resume.txt` file:

1. Go to http://127.0.0.1:5000
2. Upload `sample_resume.txt`
3. Copy a job description from `SAMPLE_JOB_DESCRIPTIONS.md`
4. Paste in the text area
5. Click "Analyze Resume"
6. View results (should get 70-85% ATS score)

### Sample Job Description for Testing
```
Position: Senior Software Engineer

Required Skills:
- 5+ years of software development experience
- Strong proficiency in Python and JavaScript
- Experience with React, Node.js, or Django
- Knowledge of cloud platforms (AWS, Azure, or GCP)
- Experience with Docker and Kubernetes
- Strong understanding of SQL and NoSQL databases
- Experience with CI/CD pipelines
- Agile/Scrum methodologies

Responsibilities:
- Design and implement scalable backend services
- Write clean, maintainable code
- Participate in code reviews
- Optimize application performance
```

---

## 🛑 Stopping the Server

Press `CTRL + C` in the terminal to stop the Flask server.

---

## 🔄 Restarting After Stopping

If you closed the terminal or stopped the server:

```bash
# 1. Navigate to project directory
cd C:\Users\baner\OneDrive\Desktop\AI-Resume_Analyzer

# 2. Activate virtual environment
.venv\Scripts\activate

# 3. Run the app
python app.py
```

---

## ⚠️ Common Issues & Solutions

### Issue 1: "python is not recognized"
**Solution:** Python is not in PATH. Use full path:
```bash
C:\Python311\python.exe app.py
```
Or reinstall Python and check "Add Python to PATH"

### Issue 2: "No module named 'flask'"
**Solution:** Virtual environment not activated or dependencies not installed:
```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

### Issue 3: "Address already in use"
**Solution:** Port 5000 is busy. Either:
- Stop the other process using port 5000
- Or change port in `app.py` (line 85):
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Changed to 5001
```

### Issue 4: "Permission denied" on uploads
**Solution:** Make sure `uploads/` folder exists and has write permissions:
```bash
mkdir uploads
```

### Issue 5: Empty white page in browser
**Solution:** 
- Check terminal for errors
- Make sure Flask is running
- Try clearing browser cache (Ctrl+Shift+R)
- Check if `templates/` and `static/` folders exist

### Issue 6: File upload fails
**Solution:**
- Check file size (must be < 16MB)
- Check file format (only PDF, DOCX, TXT)
- Check if `uploads/` folder exists

---

## 📂 Project Structure Check

Make sure you have these folders and files:

```
AI-Resume_Analyzer/
├── .venv/                  ← Virtual environment
├── app.py                  ← Main application ✓
├── requirements.txt        ← Dependencies ✓
├── templates/
│   └── index.html         ← Main page ✓
├── static/
│   ├── style.css          ← Styles ✓
│   └── script.js          ← JavaScript ✓
├── resume_parser/         ← Parser modules ✓
├── ats_score/             ← ATS modules ✓
├── job_matcher/           ← Job matching ✓
├── data/
│   ├── skills_list.txt    ← Skills database ✓
│   └── job_descriptions.csv  ← Jobs ✓
└── uploads/               ← Temp uploads folder
```

---

## 🔍 Verification Commands

### Check if Python is installed:
```bash
python --version
```
Should show: Python 3.8 or higher

### Check if virtual environment is activated:
```bash
# You should see (.venv) in your prompt
# Example: (.venv) PS C:\...\AI-Resume_Analyzer>
```

### Check if dependencies are installed:
```bash
pip list
```
Should show: Flask, PyPDF2, python-docx, scikit-learn, nltk

### Check if Flask is running:
Open http://127.0.0.1:5000 in browser

### Test the health endpoint:
```bash
# In another terminal or browser:
curl http://127.0.0.1:5000/health
```
Should return: `{"status":"healthy"}`

---

## 🌐 Accessing from Other Devices

Your app runs on all network interfaces. To access from other devices on the same network:

1. Find your IP address:
```bash
ipconfig
# Look for IPv4 Address under your active network
# Example: 192.168.1.100
```

2. Access from other device:
```
http://192.168.1.100:5000
```

**Current network access:** http://192.168.31.144:5000

---

## 🚀 Production Deployment (Optional)

For production use, don't use Flask's development server. Instead:

### Option 1: Using Gunicorn (Linux/Mac)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Option 2: Using Waitress (Windows)
```bash
pip install waitress
waitress-serve --port=5000 app:app
```

### Option 3: Deploy to Cloud
- **Heroku:** Create Procfile: `web: gunicorn app:app`
- **AWS:** Use Elastic Beanstalk
- **Azure:** Use App Service
- **Google Cloud:** Use App Engine

---

## 📊 Expected Performance

- **Startup time:** 2-3 seconds
- **Resume processing:** 1-2 seconds
- **Memory usage:** ~100-150 MB
- **Concurrent users:** 100+ (development server)
- **File size limit:** 16 MB

---

## 🎯 Daily Workflow

### Morning Startup:
```bash
cd C:\Users\baner\OneDrive\Desktop\AI-Resume_Analyzer
.venv\Scripts\activate
python app.py
```

### Work with the app:
Open http://127.0.0.1:5000

### Evening Shutdown:
Press `CTRL + C` in terminal

---

## 📝 Customization Tips

### Add More Skills
Edit `data/skills_list.txt`:
```
rust
golang
vue.js
svelte
```

### Add More Jobs
Edit `data/job_descriptions.csv`:
```csv
title,company,location,skills,description
Web Developer,Startup Co,Remote,javascript,react,node.js,Build web apps
```

### Change Port
Edit `app.py` (line 85):
```python
app.run(debug=True, host='0.0.0.0', port=8080)
```

### Change Upload Limit
Edit `app.py` (line 14):
```python
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # 32MB
```

---

## ✅ Success Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created (`.venv/`)
- [ ] Virtual environment activated (see `(.venv)` in prompt)
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Flask app running (`python app.py`)
- [ ] Browser shows app at http://127.0.0.1:5000
- [ ] Can upload resume file
- [ ] Can see results

---

## 🆘 Getting Help

### Check Terminal Output
Look for error messages in the terminal where Flask is running

### Check Browser Console
Press F12 in browser → Console tab → Look for errors

### Enable Debug Mode
Already enabled in `app.py`:
```python
app.run(debug=True, ...)
```

### View Logs
Flask prints all requests and errors in the terminal

---

## 🎉 You're All Set!

Your AI Resume Analyzer is ready to use!

**Current Status:** 🟢 RUNNING
**Access URL:** http://127.0.0.1:5000
**Network URL:** http://192.168.31.144:5000

**Quick Commands:**
```bash
# Start
python app.py

# Stop
CTRL + C

# Restart
python app.py
```

**Enjoy analyzing resumes! 🚀**
