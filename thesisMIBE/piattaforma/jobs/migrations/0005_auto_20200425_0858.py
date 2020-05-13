# Generated by Django 3.0.5 on 2020-04-25 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_remove_post_job_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_job',
            name='email_referente',
            field=models.CharField(default='SOME STRING', max_length=20),
        ),
        migrations.AddField(
            model_name='post_job',
            name='nome_azienda',
            field=models.CharField(default='SOME STRING', max_length=20),
        ),
        migrations.AlterField(
            model_name='post_job',
            name='descrizione',
            field=models.TextField(max_length=60),
        ),
        migrations.AlterField(
            model_name='post_job',
            name='posizione',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post_job',
            name='requisiti',
            field=models.TextField(max_length=60),
        ),
    ]