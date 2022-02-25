from django.shortcuts import render
from .models import Projects

app_name = "projects"

def get_projects():
    return Projects.objects.all().order_by('order_number')
