# Generated by Django 4.0 on 2022-02-02 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_alter_contact_order_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of contact info', max_length=100)),
                ('info', models.CharField(help_text='Contact info', max_length=200)),
                ('type', models.CharField(choices=[('PH', 'Phone Number'), ('LI', 'Link'), ('EM', 'Email Address'), ('TE', 'Other Text')], help_text='What kind of contact information is this?', max_length=2)),
                ('order_no', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='order_no',
            field=models.IntegerField(),
        ),
    ]