# Generated by Django 3.0.5 on 2020-04-23 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_post_job_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_job',
            old_name='company',
            new_name='student',
        ),
    ]