from django.shortcuts import render
from .models import Experience

def get_experience():
    return Experience.objects.all().order_by('-starting_year')