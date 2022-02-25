from django.shortcuts import render
from .models import Owner
from django.http import HttpResponse

app_name = 'owner'

# Create your views here.


def owner_info():
    owner = Owner.objects.first()
    return owner
