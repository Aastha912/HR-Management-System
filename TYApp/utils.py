import re
import docx2txt
import PyPDF2
from django.core.files.storage import FileSystemStorage
import os
from django.shortcuts import render

def extract_text_from_docx(docx_path):
    text = docx2txt.process(docx_path)
    return text

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def match_developer(resume_text, job_position):
    # Define keywords related to different job positions
    job_position_keywords = {
    'java_developer': ['java', 'spring', 'hibernate', 'software development', 'J2EE', 'REST API'],
    'web_designing': ['web designing', 'html', 'css', 'javascript', 'ui/ux', 'responsive design'],
    'devops_engineer': ['devops', 'continuous integration', 'deployment', 'automation', 'AWS', 'Docker'],
    'data_science': ['data science', 'machine learning', 'statistics', 'python', 'pandas', 'numpy'],
    'testing': ['testing', 'quality assurance', 'automation testing', 'manual testing', 'Selenium'],
    'database_management': ['database management', 'sql', 'mysql', 'postgresql', 'database optimization'],
    
    }

    keywords = job_position_keywords.get(job_position, [])

    if not keywords:
        return 0

    # Count the number of keywords related to the selected job position present in the resume
    keyword_count = sum(keyword.lower() in resume_text.lower() for keyword in keywords)

    # Calculate the percentage of matching keywords
    match_percentage = (keyword_count / len(keywords)) * 100

    return match_percentage


def extract_name_and_skills(resume_text):
    # Extracting name and skills from the resume text
    name_patterns = [
        re.compile(r'Name\s*:\s*([\w\s]+)', re.IGNORECASE),
        re.compile(r'(\w+\s+\w+)', re.IGNORECASE),  # Additional pattern for name
    ]

    skills_pattern = re.compile(r'Skills\s*:\s*([\w\s,]+)', re.IGNORECASE)

    name, skills = None, None

    # Try each name pattern
    for name_pattern in name_patterns:
        name_match = name_pattern.search(resume_text)
        if name_match:
            name = name_match.group(1).strip()
            break  # If a match is found, exit the loop

    skills_match = skills_pattern.search(resume_text)
    if skills_match:
        skills = skills_match.group(1).strip()

    return name, skills

def extract_projects(resume_text):
    # Extracting projects and their durations from the resume text
    projects_pattern = re.compile(r'Projects\s*:(.*?)(?:(?:Education)|(?:Skills)|\Z)', re.IGNORECASE | re.DOTALL)
    projects_match = projects_pattern.search(resume_text)

    projects = projects_match.group(1).strip() if projects_match else None

    return projects

def extract_education(resume_text):
    # Extracting education information from the resume text
    education_pattern = re.compile(r'Education\s*:(.*?)(?:(?:Projects)|(?:Skills)|(?:Experience)|\Z)', re.IGNORECASE | re.DOTALL)
    education_match = education_pattern.search(resume_text)

    education = education_match.group(1).strip() if education_match else None

    return education

def extract_experience(resume_text):
    # Extracting past work experience from the resume text
    experience_pattern = re.compile(r'Experience\s*:(.*?)(?:(?:Projects)|(?:Skills)|(?:Education)|\Z)', re.IGNORECASE | re.DOTALL)
    experience_match = experience_pattern.search(resume_text)

    experience = experience_match.group(1).strip() if experience_match else None

    return experience


