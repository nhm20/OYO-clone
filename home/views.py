from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def index(request):
    # print(request)
    return render(request, 'index.html')

class HomeView(View):
    template_name = 'index.html'
    def get(self,request):
        return render(request, self.template_name)
    def post(self,request):
        return render(request, self.template_name)