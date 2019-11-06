from django.shortcuts import render
from .models import Job

def home(request):
    return render(request, 'home.html', {'jobs':Job.objects})