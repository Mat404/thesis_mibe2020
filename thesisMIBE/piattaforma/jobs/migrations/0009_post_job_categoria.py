# Generated by Django 3.0.5 on 2020-04-30 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_remove_post_job_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_job',
            name='categoria',
            field=models.CharField(choices=[('datascience', 'DataScience'), ('productowner', 'ProductOwner'), ('businessanalyst', 'BusinessAnalyst')], default='datascience', max_length=20),
        ),
    ]
