from django.contrib.auth import authenticate

# Create your views here.


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
#

from .models import Farm
from django.template import loader
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
#
# def index(request):
#     latest_question_list = Farm.objects.order_by('-name')[:5]
#     output = ', '.join([q.name for q in latest_question_list])
#     return HttpResponse(output)

def index(request):
    latest_question_list = Farm.objects.order_by('-name')[:5]
    template = loader.get_template('app/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def profile(request):
    # latest_question_list = Farm.objects.order_by('-name')[:5]
    template = loader.get_template('app/dashboard.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    return HttpResponse(template.render( request))

def signin(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    print (username,password)
    if user is not None:
        print("Kewl")
    else:
        print ("craxy dude trying to access ")
