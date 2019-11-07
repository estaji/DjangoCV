from django.shortcuts import render
from .models import Job, Education

def home(request):
    return render(request, 'home.html', {'jobs':Job.objects, 'edus':Education.objects})