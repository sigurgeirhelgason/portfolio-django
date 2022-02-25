# Generated by Django 4.0 on 2022-01-29 00:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0005_alter_skill_skill_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill_in_procents',
            field=models.IntegerField(default=1, help_text='How good are you in this skill in procents (1-100%)', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
