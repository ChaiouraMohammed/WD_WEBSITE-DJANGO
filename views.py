from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import User
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

def home(request):
    return render(request, 'sqlForDataAPP/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(
            subject,
            f'From: {name} <{email}>\n\n{message}',
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return HttpResponse('Your message has been sent. Thank you!')

    return render(request, 'sqlForDataAPP/contact.html')

def about(request):
    return render(request, 'sqlForDataAPP/about.html')


def login(request):
    return render(request, 'sqlForDataAPP/login.html')


def registration(request):
    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')

    return render(request, 'sqlForDataAPP/registration.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'sqlForDataAPP/login.html')



def Post_1(request):
    return render(request, 'sqlForDataAPP/Post_1.html')