# Generated by Django 4.0 on 2022-01-29 13:32

from django.db import migrations, models
import education.models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_alter_education_ending_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='ending_year',
            field=models.IntegerField(default=education.models.current_year, verbose_name='ending_year'),
        ),
        migrations.AlterField(
            model_name='education',
            name='stating_year',
            field=models.IntegerField(default=education.models.current_year, verbose_name='starting_year'),
        ),
    ]
