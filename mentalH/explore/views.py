from django.shortcuts import render, redirect
from .forms import BookSession, UserRegistrationForm, LoginForm
from django.contrib.auth import login, authenticate
from django.shortcuts import get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from . import views




def index(request):
    return render(request, 'index.html')

def Anxity(request):
    return render(request, 'Anxity.html')

def community(request):
    return render(request, 'community.html')

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

@login_required
def counseling(request):
    if request.method == 'POST':
        form = BookSession(request.POST, request.FILES)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
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
            login(request)
            return redirect('counseling')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect ('counseling')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})