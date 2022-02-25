from django.shortcuts import render
from .models import Education

def get_education():
    return Education.objects.all().order_by('-starting_year')