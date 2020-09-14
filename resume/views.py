from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Job, Education, Skill, Language, Honor, SoftSkill, Jumbotron

def home(request):
    return render(request, 'home.html', {'jobs':Job.objects, 'edus':Education.objects, 'skill':Skill.objects, 'langs':Language.objects, 'honors':Honor.objects, 'softskill':SoftSkill.objects, 'jumbotron':Jumbotron.objects.first})