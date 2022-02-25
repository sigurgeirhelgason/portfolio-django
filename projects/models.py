from django.db import models
from django.core.exceptions import ValidationError


def file_size(value): # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')

class Projects(models.Model):
    order_number = models.IntegerField()
    title = models.CharField(max_length=100)
    info = models.TextField(null=True, blank=True)
    image = models.ImageField(default='default-thumbnail.jpg', validators=[file_size])
    link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
