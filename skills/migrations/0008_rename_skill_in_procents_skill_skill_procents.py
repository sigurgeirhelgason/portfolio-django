# Generated by Django 4.0 on 2022-01-29 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0007_rename_skill_set_number_skill_skill_set'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skill_in_procents',
            new_name='skill_procents',
        ),
    ]
