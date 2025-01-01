from django.shortcuts import render
from django.http import HttpResponse
#def home(request):
   # return HttpResponse("Home page")
def home(request):
    return render(request,'first_app/home.html')

