import os
import PyPDF2
import docx

def extract_text_from_pdf(filepath):
    """Extract text from PDF, DOCX, or TXT files"""
    text = ""
    
    try:
        file_extension = filepath.lower().split('.')[-1]
        
        if file_extension == 'pdf':
            with open(filepath, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
        
        elif file_extension == 'docx':
            doc = docx.Document(filepath)
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
        
        elif file_extension == 'txt':
            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()
        
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")
        
        return text.strip()
    
    except Exception as e:
        raise Exception(f"Error extracting text: {str(e)}")
