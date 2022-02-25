from django.shortcuts import render
from .models import SkillSet, Skill

# Create your views here.

def get_skill_sets():
    skill_sets = SkillSet.objects.all().order_by('order_number')
    return  skill_sets

def get_skills():
    return Skill.objects.all()