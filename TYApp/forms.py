from django import forms
from .models import JobApplication
from .models import Announcementtable
from .models import RecentProject
from .models import Documentupload
from .models import SelectedCandidate

class DocumentuploadForm(forms.ModelForm):
    class Meta:
        model = Documentupload
        fields = ['name', 'file']

        
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['full_name', 'email', 'mobile', 'remark', 'document']        

class AnnouncementtableForm(forms.ModelForm):
    class Meta:
        model = Announcementtable
        fields = '__all__'
        
class RecentProjectForm(forms.ModelForm):
    class Meta:
        model = RecentProject
        fields = ['project_name', 'project_number', 'number_of_employees', 'status']

class SelectedCandidateForm(forms.ModelForm):
    class Meta:
        model = SelectedCandidate
        fields = ['fullname', 'profession', 'status', 'score']