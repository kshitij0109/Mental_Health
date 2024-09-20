from django.shortcuts import render, redirect
from .forms import BookSession, UserRegistrationForm
from django.contrib.auth import login


def index(request):
    return render(request, 'index.html')

def Anxity(request):
    return render(request, 'Anxity.html')

def community(request):
    return render(request, 'community.html')

# def counseling(request):
#     return render(request, 'counseling.html')

def Depression(request):
    return render(request, 'Depression.html')

def feedback(request):
    return render(request, 'feedback.html')

def library(request):
    return render(request, 'library.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def StressManagement(request):
    return render(request, 'StressManagement.html')

def success(request):
    return render(request, 'success.html')

def counseling(request):
    if request.method == 'POST':
        form = BookSession(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = BookSession()
    return render(request, 'counseling.html', {'form': form})



def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form':form})