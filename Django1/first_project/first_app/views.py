from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import *


# Create your views here.
def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dic={'access_records':webpages_list}
    my_dic={'insert_me':"Hello i am from first_app"}
    return render(request, 'first_app\index.html',context=date_dic)
