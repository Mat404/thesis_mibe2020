from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Questions(models.Model):
    CAT_CHOICES = (
    ('datascience', 'DataScience'),
    ('productowner', 'ProductOwner'),
    ('businessanalyst', 'BusinessAnalyst'),
    #('sports','Sports'),
    #('movies','Movies'),
    #('maths','Maths'),
    #('generalknowledge','GeneralKnowledge'),


)


    question = RichTextField(blank=True, null= True)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    catagory = models.CharField(max_length=20, choices = CAT_CHOICES)
    student = models.ManyToManyField(User)
    class Meta:
        ordering = ('-catagory',)

    def __str__(self):
        return self.question
