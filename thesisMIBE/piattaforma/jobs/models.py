from django.db import models
from django.contrib.auth.models import User



# Create your models here.
LAVORO_CHOICES = (
    ('datascience', 'DataScience'),
    ('productowner', 'ProductOwner'),
    ('businessanalyst', 'BusinessAnalyst'),)

# declaring a Student Model


class post_job(models.Model):

    posizione= models.CharField(max_length=20)
    descrizione= models.TextField(max_length=60)
    requisiti= models.TextField(max_length=60)
    nome_azienda= models.CharField(max_length=20, default=' inserisci nome')
    email_referente= models.CharField(max_length=20, default='inserisci email')
    categoria = models.CharField(
      max_length = 20,
      choices = LAVORO_CHOICES,
      default = 'datascience'
      )




    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.posizione
