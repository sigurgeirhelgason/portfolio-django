# Generated by Django 4.0 on 2022-01-29 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0009_rename_skill_procents_skill_procents_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillset',
            name='number',
        ),
    ]
