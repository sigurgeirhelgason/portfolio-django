from django.shortcuts import render
from owner import views as owner_view
from skills import views as skill_view
from experience import views as experience_view
from education import views as education_view
from projects import views as projects_view
from contacts import views as contacts_view
from games import stafaleikur


def homepage(request):
    owner = owner_view.owner_info()
    skill_sets = skill_view.get_skill_sets()
    skills = skill_view.get_skills()
    experience = experience_view.get_experience()
    education = education_view.get_education()
    projects = projects_view.get_projects()
    contacts = contacts_view.get_contacts()
    links = contacts_view.get_links()
    return render(request,
                  'base.html',
                  {"owner": owner,
                   "skill_sets": skill_sets,
                   "skills": skills,
                   "education": education,
                   "experience": experience,
                   "projects": projects,
                   "contacts": contacts,
                   "links" : links
                   })

def stafaleikur(request):
    return render(request,
                  'stafaleikur.html')

def korg(request):
    return render(request,
                  'korg.html')