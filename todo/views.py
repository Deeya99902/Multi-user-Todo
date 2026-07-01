from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate , login as loginUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from todo.forms import TodoForm

def home(request):
    form = TodoForm()
    return render(request,'home.html' , context={'form' : form})


def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', context={"form": form})

    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        loginUser(request, user)
        return redirect('home')

    return render(request, 'login.html', context={"form": form})


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
        context ={
         "form":form
        }
        if form.is_valid():
            user=form.save()
            print(user)
            if user is not None:
                return redirect('login')
        
        else:
            return render(request,'signup.html', context=context)
        
        
           
    


   