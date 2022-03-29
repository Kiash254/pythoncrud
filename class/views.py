from pyexpat import model
from attr import fields
from django.urls import reverse_lazy
from .models import Student
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
# Create your views here.

#class based views
#Listview

class Studlist(ListView):
    model=Student
    context_object_name='class:students'

#createview
class Studecreate(CreateView):
    model=Student
    fields='__all__'
    success_url=reverse_lazy('class:students')

#detailview


class Studedetail(DetailView):
    model=Student

    fields='__all__'
    success_url=reverse_lazy('class:students'),

class studeupdate(UpdateView):

    model=Student
    fields='__all__'
    success_url=reverse_lazy('class:students')

class studeDelete(DeleteView):

    model=Student
    success_url=reverse_lazy('class:students')









