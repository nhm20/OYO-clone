from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # print(request)
    return render(request, 'index.html')

def dynamic_url(request,id,name):
   print(f"ID: {id}, Name: {name}")
   return render(request,'dynamic_url.html', {'id': id, 'name': name})
#    return render(request,'dynamic_url.html', context={'id': id, 'name': name})
