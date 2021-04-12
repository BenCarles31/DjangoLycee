from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse
from .models import Cursus,Student, Presence
from django.views.generic.edit import CreateView, UpdateView
from .forms import StudentForm, PresenceForm
from django.template import loader
from django.shortcuts import get_object_or_404

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
    
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))


def detailpresence(request,presence_id):
  result = get_object_or_404(Presence, pk=presence_id)
  student = Student.objects.get(id=result.students.id)
  template = loader.get_template('lycee/student/Presence.html')
  context = {
    'liste' : result,
    'student' :student,
  }
  return HttpResponse(template.render(context ,request))

class PresenceCreateView(CreateView):
  model = Presence
  form_class = PresenceForm
  template_name = "lycee/student/Presence.html"

  def get_success_url(self):
    return reverse ("detailpresence", args=(self.object.pk,))

def callofroll(request):
  if request.method == 'POST':
    date = request.POST.get("date")
    for student in Student:
      missing = request.POST.get('student'+str(student.id), "off")