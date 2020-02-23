from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView, 
                                ListView, DetailView,
                                CreateView , UpdateView , 
                                DeleteView )
from . import models

class IndexView(TemplateView):
    template_name = 'basicapp/index.html'

    #def get_context_data(self,**kwargs):
    #    context  = super().get_context_data(**kwargs)
    #    context['injectme'] = "Basic Injection!"
    #    return context

class SchoolListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'
    # context_object_name jest widoczny w pliku school detail pod nazwą albo school_list albo jak u nas schools
    # Example of making your own:
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail' # sprawdzić czy działa bez tego 
    model = models.School
    template_name = 'basicapp/school_detail.html' # sprawdzić czy działa bez tego 


class SchoolCreateView(CreateView):
    fields = ("name","principal","location")
    model = models.School
    # django automaticly search for template school_form.html -> <model>_form.html

class SchoolUpdateView(UpdateView):
    fields = ("name","principal")
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basicapp:list")





#def index(request):
#    return render(request, 'basicapp/index.html')
