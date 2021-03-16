from django.db import models

# Create your models here.
class Cursus(models.Model):
 name = models.CharField(
    verbose_name="Cursus Name :",
    max_length=255,
    blank=True,
    null=False,
    default='',
    help_text='Nom du cursus :'
  )
 year_from_bac = models.SmallIntegerField(
    verbose_name="Year from BAC :",
    blank=True,
    null=False,
    default=0,
    help_text='Annee depuis le bac :'
  )
 scholar_year = models.CharField(
    verbose_name="Year from BAC :",
    blank=True,
    null=False,
    default='0000-0001',
    help_text='Annee depuis le bac :'
  )
  def __str__(self):
    return '{} {}'.format(self.name, self.scholar_year)

class Students(models.Model):
  first_name = models.CharField(
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
    verbose_name="Date of birth :",
    max_length=50,
    blank=False,
    null=False,
    default='???',
    help_text='date de naissance de l etudiant'
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
  null=True,
  related_name="student_name"
)
 



















 
