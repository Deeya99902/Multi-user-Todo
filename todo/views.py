from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context ={
         "form":form
        }
        return render(request,'signup.html', context=context)

    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            return HttpResponse("Form is valid")
        else:
            return HttpResponse("Form is invalid")
    


   