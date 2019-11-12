from django.shortcuts import render
from .models import Job, Education, Skill

def home(request):
    return render(request, 'home.html', {'jobs':Job.objects, 'edus':Education.objects, 'skill':Skill.objects})