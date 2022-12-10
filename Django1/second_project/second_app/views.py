from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User

# Create your views here.
def index(request):
    my_dic={'insert_me':"Hello i am from first_app"}
    return render(request, 'second_app\index.html',context=my_dic)
# def help(request):
#     help_dic={'help_insert':"Help Page"}
#     return render(request, 'second_app\index.html',context=help_dic)

def users(request):
    user_list=User.objects.order_by('first_name')
    user_dict={'users':user_list}
    return render(request,'second_app/users.html',context=user_dict)
