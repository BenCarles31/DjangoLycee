# Generated by Django 3.1.7 on 2021-03-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', help_text='Nom du cursus :', max_length=255, verbose_name='Cursus Name :')),
                ('year_from_bac', models.CharField(blank=True, default='', help_text='Annee depuis le bac :', max_length=255, verbose_name='Year from BAC :')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(default='', verbose_name='Date of birth :')),
                ('last_name', models.CharField(default='???', help_text='date de naissance de l etudiant', max_length=50, verbose_name='Date of birth :')),
                ('phone_number', models.CharField(blank=True, default='0123456789', help_text='numero de telephone', max_length=10, verbose_name='Phone number :')),
                ('email', models.CharField(default='???@???.com', help_text='Courriel', max_length=255, verbose_name='Email :')),
                ('comments', models.CharField(blank=True, default='', help_text='Commentaires :', max_length=255, verbose_name='Comments :')),
            ],
        ),
    ]
