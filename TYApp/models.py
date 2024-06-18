# models.py
from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
class Documentupload(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class RecentProject(models.Model):
    project_name = models.CharField(max_length=100)
    project_number = models.CharField(max_length=10)
    number_of_employees = models.IntegerField()
    status = models.CharField(max_length=20)
    
class Etable(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_pin = models.IntegerField()
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10)
    department = models.CharField(max_length=10)
    role = models.CharField(max_length=20)    
    
class JobApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    remark = models.TextField()
    document = models.FileField(upload_to='job_applications/documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
class JobApplication2(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    remark = models.TextField()
    document = models.FileField(upload_to='job_applications/documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
            
class Announcementtable(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='announcement_images/')
    position = models.CharField(max_length=100)
    qualification_experience = models.TextField()
    job_description = models.TextField()
    event_date = models.DateField()
    expected_salary = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    JOB_TYPES = [
        ('full_time', 'Full Time'),
        ('fresher', 'Fresher'),
        ('internship', 'Internship'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('temporary', 'Temporary'),
    ]
    job_type = models.CharField(max_length=20, choices=JOB_TYPES)

    def __str__(self):
        return self.title
    
class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_no = models.CharField(max_length=20)
    number_of_employees = models.IntegerField(default=0)
    manager = models.CharField(max_length=100)
    progress = models.FloatField(default=0.0)
    employee_name1 = models.CharField(max_length=100, blank=True, null=True)
    employee_name2 = models.CharField(max_length=100, blank=True, null=True)
    employee_name3 = models.CharField(max_length=100, blank=True, null=True)
    employee_name4 = models.CharField(max_length=100, blank=True, null=True)
    employee_no1 = models.CharField(max_length=20, blank=True, null=True)
    employee_no2 = models.CharField(max_length=20, blank=True, null=True)
    employee_no3 = models.CharField(max_length=20, blank=True, null=True)
    employee_no4 = models.CharField(max_length=20, blank=True, null=True)
    role_employee1 = models.CharField(max_length=100, blank=True, null=True)
    role_employee2 = models.CharField(max_length=100, blank=True, null=True)
    role_employee3 = models.CharField(max_length=100, blank=True, null=True)
    role_employee4 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.project_name
    
class CompanyEmployeeCount(models.Model):
    company = models.CharField(max_length=100)
    employee_count = models.IntegerField()

    def __str__(self):
        return f"{self.company} - {self.employee_count}"
    
class SelectedCandidate(models.Model):
    fullname = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return self.fullname