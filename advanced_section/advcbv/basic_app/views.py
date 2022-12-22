from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
from . import models
# from django.http import HttpResponse


#  functinal views.
# def index(request):
#     return render(request,'index.html')

# Class based views
# class CBView(V|iew):
#     def get(self,request):
#         return HttpResponse("Claass Based Views Are Cool!")

# Template views with CBV
class IndexView(TemplateView):
    template_name='index.html'

#     def get_context_data(self,**kwargs):
#         context=super().get_context_data(**kwargs)
#         context['injectme']='BASIC INJECTION!'
#         return context
# List View
class SchoolListView(ListView):  #school ko list dekhuxa
    context_object_name='schools'
    model=models.School
    # template_name='basic_app/school_list.html'


# Detail View
class SchoolDetailView(DetailView): # school ko details dekhuxa
    context_object_name='school_detail'
    model=models.School
    template_name='basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields=('name','principal','location')
    model=models.School
# view for update
class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model=models.School

#views for DeleteViewc
class SchoolDeleteView(DeleteView):
    model=models.School
    success_url=reverse_lazy("basic_app:list")
