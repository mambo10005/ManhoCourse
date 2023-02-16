#from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home/index.html', context=context)