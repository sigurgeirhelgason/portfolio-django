from django.core.exceptions import ValidationError
from django.db import models

def file_size(value): # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    about_info = models.TextField()
    home_info = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    photo = models.ImageField(default='default-profile.png', blank=True, validators=[file_size])

    def __str__(self):
        return self.name

    #to make sure there is only one owner in database
    def save(self, *args, **kwargs):
        if not self.pk and Owner.objects.exists():
            raise ValidationError('There is can be only one Owner instance')
        return super(Owner, self).save(*args, **kwargs)