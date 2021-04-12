from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse
from .models import Cursus,Student
from django.views.generic.edit import CreateView, UpdateView
from .forms import StudentForm
from django.template import loader

def index(request):
  result_list = Cursus.objects.order_by('name')
  #charge le template
  
  template = loader.get_template('lycee/index.html')
  
  #Contexte
  context = {
    'liste' : result_list,
  }
  #return HttpResponse(template.render(context, request))
  return render( request , 'lycee/index.html', context)


def detail(request, cursus_id):

  result_list = Student.objects.filter(cursus=cursus_id)
  
 #Contexte
  context = {'liste' : result_list}
  return render( request , 'lycee/cursus/student_list.html', context)
 
 
def detail_student(request, student_id):
  result_list = Student.objects.get(pk=student_id)
  
 #Contexte
  context = {'liste' : result_list}
  return render( request , 'lycee/student/detail_student.html', context)
  
class StudentCreateView(CreateView):
  #le modele auquel on se refere
  model = Student
  #Le formulaire associé (dans form.py)
  form_class = StudentForm
  #nom du template
  template_name = 'lycee/student/create.html'

#Surcharge de la methode get_success_url
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

class ModifyStudent(UpdateView):
  model = Student
  form_class = StudentForm
  template_name = "lycee/student/edit.html"