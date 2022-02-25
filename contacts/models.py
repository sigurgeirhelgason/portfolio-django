from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Link(models.Model):
    TYPE_CHOICES = (
        ("PH", _("Phone Number")),
        ("LI", _("Link")),
        ("EM", _("Email Address")),
        ("TE", _("Other Text"))
    )

    title = models.CharField(max_length=100, help_text="Title of contact info")
    info = models.CharField(max_length=200, help_text="Contact info")
    type = models.CharField(max_length=2, help_text="What kind of contact information is this?", choices=TYPE_CHOICES)
    order_no = models.IntegerField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    TYPE_CHOICES = (
        ("PH", _("Phone Number")),
        ("LI", _("Link")),
        ("EM", _("Email Address")),
        ("TE", _("Other Text"))
    )

    title = models.CharField(max_length=100, help_text="Title of contact info")
    info = models.CharField(max_length=200, help_text="Contact info")
    type = models.CharField(max_length=2, help_text="What kind of contact information is this?", choices=TYPE_CHOICES)
    order_no = models.IntegerField()

    def __str__(self):
        return self.title