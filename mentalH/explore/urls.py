from django.urls import path, include
from . import views
from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    
   path('', views.index, name='index'),
    path('Anxity/', views.Anxity, name='Anxity'),
    path('community/', views.community, name='community'),
    path('counseling/', views.counseling, name='counseling'),
    path('Depression/', views.Depression, name='Depression'),
    path('library/', views.library, name='library'),
    path('feedback/', views.feedback, name='feedback'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('StressManagement/', views.StressManagement, name='StressManagement'),
    path('counseling/success/', views.success, name='success_url'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),

]
