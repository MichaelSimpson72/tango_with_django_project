from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'aboutmessage': 'This tutorial has been put together by Mick Simpson'}

    return render(request, 'rango/about.html', context=context_dict)