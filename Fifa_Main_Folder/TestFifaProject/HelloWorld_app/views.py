from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    my_dict = {'insert_me': "Hello I am from thomas"}
    return render(request, 'HelloWorld_app/index.html', context=my_dict)

def help(request):
    help_dict = {'insert_me': "Sorry no furthere help available!"}
    return render (request, 'help.html', context= help_dict)
