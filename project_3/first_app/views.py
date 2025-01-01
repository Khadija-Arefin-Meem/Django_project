from django.shortcuts import render

# Create your views here.
def home(request):
    d={'author' : 'Meem','age': 23,'courses':[
        {
            'id' :1,
            'name':'python',
            'fee':5000,
        },
        {
            'id' :2,
            'name':'Django',
            'fee':1000,
        },

    ]}
    return render(request,'home.html',d)