from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dic={'insert_me':"Hello i am from first_app"}
    return render(request, 'first_app\index.html',context=my_dic)
def help(request):
    help_dic={'help_insert':"Help Page"}
    return render(request, 'second_app\index.html',context=help_dic)
