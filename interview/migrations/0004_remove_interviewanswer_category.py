# Generated by Django 4.1.5 on 2023-03-18 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0003_interviewanswer_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviewanswer',
            name='category',
        ),
    ]
