from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

email_domains = {
    'gmail.com': 'https://mail.google.com/',
    'yahoo.com': 'https://mail.yahoo.com/',
    'outlook.com': 'https://outlook.live.com/',
    'aol.com': 'https://mail.aol.com/',
    'icloud.com': 'https://www.icloud.com/mail/',
    'hotmail.com': 'https://outlook.live.com/',
    'mail.com': 'https://www.mail.com/',
    'protonmail.com': 'https://mail.protonmail.com/',
    'yandex.com': 'https://mail.yandex.com/',
    'msn.com': 'https://outlook.live.com/',
}


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # check if user exists
        user = User.objects.filter(email=email).first()
        if user is not None and user.is_active:
            authenticated_user = authenticate(request, username=email, password=password)
            if authenticated_user is not None:
                messages.error(request, 'User logged in successfully')
                return render(request, 'users/login.html')
            else:
                messages.error(request, 'Email address or password is incorrect')
                return render(request, 'users/login.html')
        elif user is not None and not user.is_active:
            domain = user.username.split('@')[1]
            if domain in email_domains:
                link = email_domains[domain]
                msg = mark_safe(f'User is not active, check your <a href={link}>email</a> to activate your account')
            else:
                msg = 'User is not active, check your email to activate your account'
            messages.error(request, msg)
            return render(request, 'users/login.html')
        else:
            messages.error(request, 'Email address or password is incorrect')
            return render(request, 'users/login.html')

    return render(request, 'users/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirm_password']

        if password == password2:
            # check if username exists
            if User.objects.filter(email=username).exists():
                messages.error(request, 'Email address is already in use')
                return render(request, 'users/register.html')
            else:
                user = User.objects.create_user(username=username, password=password, email=username)
                user.save()
                messages.success(request, 'User created successfully, check your email to activate your account')
                return redirect('login')
    return render(request, 'users/register.html')


def activate(request):
    return render(request, 'users/activate.html')