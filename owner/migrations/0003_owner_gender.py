# Generated by Django 4.0 on 2022-01-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_owner_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='gender',
            field=models.CharField(default='other', max_length=100),
        ),
    ]
