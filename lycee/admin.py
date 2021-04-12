from django.contrib import admin

# Register your models here

from .models import Student, Cursus, Presence

class StudentAdmin(admin.ModelAdmin):
  list_display = ("first_name","last_name","email", "phone_number")

class CursusAdmin(admin.ModelAdmin):
 # fields = ("scholar_year","name","year_from_bac")
  fieldsets = [
   ('nom_zone1', {'fields': ['name']}),
   ('nom_zone2', {'fields':
   ['scholar_year','year_from_bac'], 'classes':
   ['collapse']}),
  ]

class PresenceAdmin(admin.ModelAdmin):
  fields = ('Cause','date','ismissing', 'student')

admin.site.register(Student,StudentAdmin)
admin.site.register(Cursus, CursusAdmin)
admin.site.register(Presence, PresenceAdmin)
