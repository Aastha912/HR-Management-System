from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.db.models.functions import TruncWeek
from django.contrib.auth.decorators import login_required
from .models import RecentProject
from .models import Etable, Project
from .forms import DocumentuploadForm
from .models import Documentupload
from .forms import AnnouncementtableForm
from .models import Announcementtable
from .forms import SelectedCandidateForm
from .models import SelectedCandidate
from .models import Etable
from .models import Documentupload 
from .models import Announcementtable
from .forms import AnnouncementtableForm
from .forms import RecentProjectForm

from .forms import JobApplicationForm
from .models import JobApplication
from .models import CompanyEmployeeCount
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.db.models import Count
import calendar
from .models import RecentProject
from datetime import datetime
import pickle
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import PyPDF2
from io import BytesIO
from docx import Document
from .utils import (
    extract_text_from_docx,
    extract_text_from_pdf,
    match_developer,
    extract_name_and_skills,
    extract_projects,
    extract_education,
    extract_experience,
)


# Loading models
clf = pickle.load(open('C:\\Users\\Aastha\\OneDrive\\Desktop\\TYDjango\\TYProject\\TYApp\\model\\clf (1).pkl', 'rb'))
tfidfd = pickle.load(open('C:\\Users\\Aastha\\OneDrive\\Desktop\\TYDjango\\TYProject\\TYApp\\model\\tfidf.pkl', 'rb'))


def clean_resume(resume_text):
    clean_text = re.sub('http\S+\s*', ' ', resume_text)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+', '', clean_text)
    clean_text = re.sub('@\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    return clean_text

def extract_text_from_pdf(pdf_file):
    text = ''
    with pdf_file as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    paragraphs = [paragraph.text for paragraph in doc.paragraphs]
    return '\n'.join(paragraphs)

def predict_category(resume_text):
    cleaned_resume = clean_resume(resume_text)
    input_features = tfidfd.transform([cleaned_resume])
    prediction_id = clf.predict(input_features)[0]

    category_mapping = {
         15: "Java Developer",
            23: "Testing",
            8: "DevOps Engineer",
            20: "Python Developer",
            24: "Web Designing",
            12: "HR",
            13: "Hadoop",
            3: "Blockchain",
            10: "ETL Developer",
            18: "Operations Manager",
            6: "Data Science",
            22: "Sales",
            16: "Mechanical Engineer",
            1: "Arts",
            7: "Database",
            11: "Electrical Engineering",
            14: "Health and fitness",
            19: "PMO",
            4: "Business Analyst",
            9: "DotNet Developer",
            2: "Automation Testing",
            17: "Network Security Engineer",
            21: "SAP Developer",
            5: "Civil Engineer",
            0: "Advocate",
    }

    category_name = category_mapping.get(prediction_id, "Unknown")
    return category_name

# ... (previous code)

def userPage(request):
    query = request.GET.get('q')
    announcements = Announcementtable.objects.all()
    if query:
        announcements = announcements.filter(title__icontains=query)
    context = {
        'announcements': announcements
    }
    if request.method == 'POST' and request.FILES.get('resume_file'):
        uploaded_file = request.FILES['resume_file']

        # Check if the file has a valid extension
        valid_extensions = ['.txt', '.pdf']
        if not any(uploaded_file.name.lower().endswith(ext) for ext in valid_extensions):
            return render(request, 'user.html', {'error': 'Invalid file format. Please upload a .txt or .pdf file.'})

        try:
            if uploaded_file.name.lower().endswith('.pdf'):
                resume_text = extract_text_from_pdf(uploaded_file)
            elif uploaded_file.name.lower().endswith('.docx'):
                return render(request, 'user.html', {'error': 'Invalid file format. Please upload a .txt or .pdf file.'})
            else:
                resume_text = uploaded_file.read().decode('utf-8')
        except UnicodeDecodeError:
            resume_text = uploaded_file.read().decode('latin-1')

        category_name = predict_category(resume_text)

        # Get announcements
        announcementtable = Announcementtable.objects.all()

        # Render the result on the same page
        return render(request, 'user.html', {'announcementtable': announcementtable, 'category_name': category_name})

    # If it's not a POST request or doesn't contain resume_file
    # Get announcements
    announcementtable = Announcementtable.objects.all()
    
    return render(request, 'user.html', {'announcementtable': announcementtable})

@login_required(login_url='login')

def index(request):
    return render(request,'index.html')

def registration(request):
    if request.method=='POST':
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        umail=request.POST.get('umail')
        upass=request.POST.get('upass')

        my_user=User.objects.create_user(username,umail,upass)
        my_user.save()
        return redirect('login')
        
    return render(request,'registration.html')

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        upass=request.POST.get('upass')
        user=authenticate(request,username=username,password=upass)
        user_type = request.POST.get('user_type')
        if user is not None:
            login(request, user)
            if user_type == 'user':
                return redirect('user')  # Redirect to user dashboard
            elif user_type == 'admin':
                return redirect('dashboard')  # Redirect to admin dashboard
            elif user_type == 'organization':
                return redirect('company')  # Redirect to organization dashboard
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request,'login.html')

def dashboard(request):
    if request.method == 'POST':
        form = RecentProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  
    else:
        form = RecentProjectForm()  
        recent_projects = RecentProject.objects.all()  # Moved the assignment here
    
    month_calendar = calendar.monthcalendar(datetime.now().year, datetime.now().month)

    context = {
        'form': form,
        'recent_projects': recent_projects,
        'month_calendar': month_calendar,
        'current_month': datetime.now().strftime('%B')
    }
  
    return render(request, 'dashboard.html', context)

def profile(request):
    
    return render(request,'profile.html')

def organisationPage(request):
    if request.method == 'POST':
        form = DocumentuploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('organisation')  
    else:
        form = DocumentuploadForm()  
        documents = Documentupload.objects.all()  # Use Documentupload model
    
        return render(request, 'organisation.html', {'form': form, 'documents': documents})
    


def employee(request):
    etable_employee = Etable.objects.all()
    projects = Project.objects.all() 
    company_data = CompanyEmployeeCount.objects.all()

    # Extract company names and employee counts
    companies = [entry.company for entry in company_data]
    employee_counts = [entry.employee_count for entry in company_data]

    # Create the bar graph
    plt.figure(figsize=(12, 8))
    plt.bar(companies, employee_counts, color='pink')
    plt.xlabel('Company', fontsize=22)  # Increase font size for x-axis label
    plt.ylabel('Number of Candidates', fontsize=22)  # Increase font size for y-axis label
    plt.title('Number of Candidates applied in Each Company', fontsize=22)  # Increase font size for title
    plt.xticks(rotation=45, ha='right', fontsize=18)  # Increase font size for x-axis tick labels
    plt.yticks(fontsize=16)  # Rotate x-axis labels for better readability
    plt.tight_layout()


    # Convert the plot to a base64 string
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.savefig('bar_graph_transparent.png', transparent=True)
    plt.close()

    if request.method == 'POST':
        form = SelectedCandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee')  
    else:
        form = SelectedCandidateForm()  
        SelectedCandidates =SelectedCandidate.objects.all()  
    
       
    return render(request, 'employee.html', {'etable_employee': etable_employee, 'projects': projects,'plot_data': plot_data,'form': form, 'SelectedCandidates': SelectedCandidates})

def settings(request):
    
    return render(request,'settings.html')

def job_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = JobApplicationForm()
    return render(request, 'job_application.html', {'form': form})


def company(request):
    if request.method == 'POST':
        form = AnnouncementtableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('company')  # Redirect to the same page after form submission
    else:
        form = AnnouncementtableForm()  # Create a new form instance

    # Get all past announcements to display
    announcements = Announcementtable.objects.all()

    return render(request, 'company.html', {'form': form, 'announcementtable': announcements})

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .utils import (
    extract_text_from_docx,
    extract_text_from_pdf,
    match_developer,
    extract_name_and_skills,
    extract_projects,
    extract_education,
    extract_experience,
)
def resume_match(request):
    job_applications = JobApplication.objects.all()
    if request.method == 'POST' and request.FILES.getlist('resume_files'):
        uploaded_files = request.FILES.getlist('resume_files')
        job_position = request.POST.get('job_position', '')

        # List to store matched resumes
        matched_resumes = []

        for uploaded_file in uploaded_files:
            # Save the uploaded file temporarily
            fs = FileSystemStorage()
            file_path = fs.save(uploaded_file.name, uploaded_file)

            # Extract text from the uploaded file
            if file_path.lower().endswith('.docx'):
                resume_text = extract_text_from_docx(file_path)
            elif file_path.lower().endswith('.pdf'):
                resume_text = extract_text_from_pdf(file_path)
            else:
                fs.delete(file_path)  # Delete unsupported file
                continue  # Skip unsupported file formats

            # Match the Developer based on the selected job position
            match_score = match_developer(resume_text, job_position)

            # Extract information from the resume
            name, skills = extract_name_and_skills(resume_text)
            projects = extract_projects(resume_text)
            education = extract_education(resume_text)
            experience = extract_experience(resume_text)

            # Check if the match score is above the threshold
            if match_score > 15:
                matched_resumes.append({
                    'filename': uploaded_file.name,
                    'match_score': match_score,
                    'name': name,
                    'skills': skills,
                    'projects': projects,
                    'education': education,
                    'experience': experience,
                })

            fs.delete(file_path)  # Delete the temporary file

        # Display or save the matched resumes
        if matched_resumes:
            return render(request, 'resume_match.html', {'matched_resumes': matched_resumes})
        else:
            return render(request, 'resume_match.html', {'matched_resumes': None})

    return render(request, 'resume_match.html', {'matched_resumes': None,'job_applications': job_applications})
