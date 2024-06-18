from django.contrib import admin
from .models import  Etable, JobApplication, JobApplication2, RecentProject,Announcementtable,Project,CompanyEmployeeCount,Documentupload,SelectedCandidate

admin.site.register(RecentProject)
admin.site.register(Etable)
admin.site.register(Documentupload)
admin.site.register(JobApplication)
admin.site.register(JobApplication2)
admin.site.register(Announcementtable)
admin.site.register(Project)
admin.site.register(CompanyEmployeeCount)
admin.site.register(SelectedCandidate)
# Register your models here.
