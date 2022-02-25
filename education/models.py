from django.db import models
import datetime
from django.utils.translation import gettext as _

def year_choices():
   choices = [(r,str(r)) for r in reversed(range(1940, datetime.date.today().year+1))]
   return choices

def current_year():
    return datetime.date.today().year





class Education(models.Model):
    school_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, help_text="The title of degree or education")
    starting_year = models.IntegerField(_('starting_year'),
                                       choices=year_choices(),
                                       default=current_year,
                                       blank=True,
                                       null=True)
    ending_year = models.IntegerField(_('ending_year'),
                                      choices=year_choices(),
                                      default=current_year,
                                      blank=True,
                                      null=True)
    info = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.school_name}"