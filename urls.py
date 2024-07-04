from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('post1/', views.Post_1, name='post1'),
]
