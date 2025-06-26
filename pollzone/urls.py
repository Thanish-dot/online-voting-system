from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('vote/<int:candidate_id>/', views.vote, name='vote'),
    path('result/', views.result, name='result'),
    path('base/', views.base_view, name='base'),
    path('criteria/', views.criteria, name='criteria'),  
    path('proof/', views.proof, name='proof'),  
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('eligibility/', views.check_eligibility, name='check_eligibility'),

]