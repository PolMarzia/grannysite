from django.shortcuts import render, redirect
from mainsite.forms import *


# Create your views here.
def mainpage(request):
    return render(request, "index.html", locals())