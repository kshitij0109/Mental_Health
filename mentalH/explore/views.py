from urllib import request
from django.shortcuts import render, redirect
from .forms import BookSession, UserRegistrationForm, LoginForm, BookSessionForm
from django.contrib.auth import login, authenticate
from django.shortcuts import get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from . import views
from .models import CounselingQueue, CounselingSession, Session
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.functions import TruncDay




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

def queue_list(request):
    queues = Session.objects.all().order_by('-Date')
    return render(request, 'queue_list.html', {'queues': queues})

@login_required
def counseling(request):
    if request.method == 'POST':
        form = BookSession(request.POST, request.FILES)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            request.session['session_id'] = session.id
            return redirect('queue_list')
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


def logout(request):
    return render(request, 'registration/loggedOut.html')



@login_required
def book_session(request):
    if request.method == 'POST':
        form = BookSessionForm(request.POST)
        if form.is_valid():
            print("Form is valid")  
            print(request.POST)
            session_id = form.cleaned_data['session_id']
            print(session_id)  
            print(session_id.id)  
            queue = CounselingQueue.objects.create(user=request.user, session=session_id)
            queue.position = CounselingQueue.objects.filter(session=session_id).count() + 1
            queue.save()
            request.session['session_id'] = session_id.id
            request.session.save()
            print("Session saved")  # Verify that the session is saved
            return redirect('queue_view')
    else:
        form = BookSessionForm()
    return render(request, 'book_session.html',{'form':form})

@login_required
def queue_view(request):
    session_id = request.session.get('session_id')
    if session_id is None:
        return redirect('index')
    session = CounselingSession.objects.filter(id=session_id).first()
    if session is None:
        
        return redirect('index')
    user_position, created = CounselingQueue.objects.get_or_create(user=request.user, session_id=session_id)
    if created:
        user_position.position = CounselingQueue.objects.filter(session_id=session_id).count() + 1
        user_position.save()
    queue = CounselingQueue.objects.filter(session_id=session_id).order_by('position')
    users_ahead = queue.filter(position__lt=user_position.position)
    return render(request, 'queue.html', {'queue': queue, 'user_position': user_position.position, 'users_ahead': users_ahead})



def session_statistics(request):
    session_stats = {}
    for user in User.objects.all():
        num_sessions = CounselingQueue.objects.filter(user=user, status='completed').count()
        session_stats[user.username] = num_sessions
    return render(request, 'session_stats.html', {'session_stats': session_stats})


def user_registration_stats(request):
    session_dates = Session.objects.annotate(date=TruncDay('Date')).values('date').annotate(count=Count('id')).order_by('date')
    return render(request, 'user_registration_stats.html', {'session_dates': session_dates})


@login_required
def account_view(request):
    user = request.user
    booked_sessions = Session.objects.filter(user=user)
    total_sessions = booked_sessions.count()
    #active_subscriptions = user.subscriptions.filter(active=True).count()

    context = {
        'user': user,
        'booked_sessions': booked_sessions,
        'total_sessions': total_sessions,
        #'active_subscriptions': active_subscriptions,
    }

    return render(request, 'account.html', context)