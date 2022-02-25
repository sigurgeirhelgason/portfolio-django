from django.shortcuts import render
from .models import Contact
from .models import Link
# Create your views here.
def get_contacts():
    return Contact.objects.all().order_by("order_no")

def get_links():
    return Link.objects.all().order_by('order_no')