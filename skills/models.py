from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class SkillSet(models.Model):
    order_number = models.PositiveSmallIntegerField(help_text="The order the skill set should be on the page")
    title = models.CharField(max_length=100,
                             help_text="The title of the skill set")

    def __str__(self):
        return self.title


class Skill(models.Model):
    skill_set = models.ForeignKey('SkillSet',
                                  on_delete=models.CASCADE, )
    title = models.CharField(max_length=100)
    procents = models.IntegerField(
        default=1,
        help_text="How good are you in this skill in procents (0-100%)",
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return (f"{self.title} in {self.skill_set}")