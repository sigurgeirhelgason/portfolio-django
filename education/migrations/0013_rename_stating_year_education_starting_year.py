# Generated by Django 4.0 on 2022-01-30 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0012_alter_education_ending_year_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='stating_year',
            new_name='starting_year',
        ),
    ]