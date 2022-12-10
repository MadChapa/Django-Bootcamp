from django.shortcuts import render
from django.contrib import admin
from first_app import views

# Create your views here.
def index(request):
    my_dic={'insert_content':"Hello i am from first_app"}
    return render(request, 'first_app/index.html',context=my_dic)
