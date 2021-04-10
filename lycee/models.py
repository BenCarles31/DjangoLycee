from django.db import models

# Create your models here.
class Cursus(models.Model):
 name = models.CharField(
    verbose_name="Cursus Name :",
    max_length=50,
    blank=False,
    null=True,
    default='aucun',
    help_text='Nom du cursus :'
  )
 year_from_bac = models.SmallIntegerField(
    verbose_name="Year from BAC :",
    blank=False,
    null=True,
    default=0,
    help_text='Annee depuis le bac :'
  )
 scholar_year = models.CharField(
    verbose_name="Scholar year :",
    max_length=9,
    blank=False,
    default='0000-0001',
    null=True,
    help_text='Annee scolaire :'
  )
 def __str__(self):
    return '{} {}: {}'.format(self.name,self.year_from_bac,self.scholar_year)

class Student(models.Model):
 first_name = models.CharField(
    verbose_name="Prenom :",
    max_length=50,
    blank=False,      
    null=False
  )
 birth_date = models.DateField(
    verbose_name="Date of birth :",
    blank=False,
    null=False,
    default=''
  )
 last_name = models.CharField(
    verbose_name="Last Name :",
    max_length=50,
    blank=False,
    null=False,
    default='???',
    help_text='nom de famille de l etudiant'
  )
 phone_number = models.CharField(
    verbose_name="Phone number :",
    max_length=10,
    blank=True,
    null=False,
    default='0123456789',
    help_text='numero de telephone'
  )
 email = models.CharField(
   verbose_name="Email :",
    max_length=255,
    blank=False,
    null=False,
    default='???@???.com',
    help_text='Courriel'
  )
 comments = models.CharField(
    verbose_name="Comments :",
    max_length=255,
    blank=True,
    null=False,
    default='',
    help_text='Commentaires :'
  )
 cursus = models.ForeignKey(
    Cursus,
    on_delete=models.CASCADE,
    null=True
  )
 def __str__(self):
   return '{} {}'.format(self.first_name, self.last_name)