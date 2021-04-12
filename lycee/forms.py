from django.forms.models import ModelForm
from .models import Student

class StudentForm(ModelForm):

  class Meta():
    model = Student

    fields = (
      "first_name",
      "last_name",
      "birth_date",
      "phone_number",
      "email",
      "comments",
      "cursus",
    )