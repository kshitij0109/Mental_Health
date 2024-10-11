from django.urls import path, include
from . import views
from django.contrib.auth.urls import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.index, name='index'),
    path('Anxity/', views.Anxity, name='Anxity'),
    path('community/', views.community, name='community'),
    path('counseling/', views.counseling, name='counseling'),
    path('Depression/', views.Depression, name='Depression'),
    path('library/', views.library, name='library'),
    path('feedback/', views.feedback, name='feedback'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('StressManagement/', views.StressManagement, name='StressManagement'),
    path('counseling/success/', views.success, name='success_url'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/explore/counseling/', views.counseling, name='counseling'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('book-session/', views.book_session, name='book_session'),
    path('queue/', views.queue_view, name='queue_view'),
    path('queue_list/', views.queue_list, name='queue_list'),
    path('session_stats/', views.session_statistics, name='session_stats'),
    path('user-registration-stats/', views.user_registration_stats, name='user_registration_stats'),
    path('session-dates/', views.user_registration_stats, name='session_dates'),
    path('account/', views.account_view, name='account'),

]
