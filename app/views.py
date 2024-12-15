from django.shortcuts import render,HttpResponse
from django.template.loader import get_template


def index(request):
    return render(request,"homeup.html")

def about(request):
    return HttpResponse("this is about")


    

# Create your views here.
