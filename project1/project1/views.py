from django.http import HttpResponse

def home(Request):
    return HttpResponse("This is our home page")

def contact(Request):
    return HttpResponse("This is our contact page")