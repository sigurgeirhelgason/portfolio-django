# Generated by Django 4.0 on 2022-02-02 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_links_alter_contact_order_no'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Links',
            new_name='Link',
        ),
    ]