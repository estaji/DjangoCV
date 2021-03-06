from django.shortcuts import render
from .models import Job, Education, Skill, Language, Honor, SoftSkill, Jumbotron, Seo, Bar


def home(request):
    return render(request, 'home.html', {'jobs': Job.objects, 'edus': Education.objects, 'skill': Skill.objects, 'langs': Language.objects, 'honors': Honor.objects, 'softskill': SoftSkill.objects, 'jumbotron': Jumbotron.objects.first, 'seo': Seo.objects.first, 'bar': Bar.objects.first})
