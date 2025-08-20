from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hi... from Django server")

def about(request):
    return render(request,'index.html')

def contact(request):
    return HttpResponse("<h1>This is the contact page</h1>")