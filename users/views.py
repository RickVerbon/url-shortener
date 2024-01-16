from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.core.mail import send_mail
from django.conf import settings
from users.models import ActivateUser
from uuid import uuid4

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


def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # check if user exists
        user = User.objects.filter(email=email).first()
        if user is not None and user.is_active:
            authenticated_user = authenticate(request, username=email, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Email address or password is incorrect')
                return render(request, 'users/login.html')
        elif user is not None and not user.is_active:
            domain = user.username.split('@')[1]
            if domain in email_domains:
                link = email_domains[domain]
                msg = mark_safe(f'User is not active, check your <a href={link}>email</a> to activate your account<br>'
                                f"Didn't receive an email? <a href='/resend-activation'>Resend activation email</a>")
            else:
                msg = 'User is not active, check your email to activate your account'
            messages.error(request, msg)
            return render(request, 'users/login.html')
        else:
            messages.error(request, 'Email address or password is incorrect')
            return render(request, 'users/login.html')

    return render(request, 'users/login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

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
                user.is_active = False
                user.save()
                activate_user = ActivateUser(user=user, token=uuid4())
                ActivateUser.objects.create(user=user, token=activate_user.token)
                send_mail(
                    subject='Activate your account for URL Shortener',
                    message=f'Click the link to activate your account: {settings.DOMAIN}/activate/{user.token}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user.email],
                    fail_silently=False
                )
                domain = user.username.split('@')[1]
                if domain in email_domains:
                    link = email_domains[domain]
                    msg = mark_safe(f"We've sent an <a href={link}>email</a> to {user.email} to activate your account.")
                else:
                    msg = f'We have sent an email to {user.email} to activate your account.'
                messages.success(request, msg)
            return redirect('login')
    return render(request, 'users/register.html')


def activate(request, token):
    activate_user = ActivateUser.objects.filter(token=token).first()
    if activate_user is not None:
        user = activate_user.user
        user.is_active = True
        user.save()
        activate_user.delete()
        messages.success(request, 'User activated successfully')
        return redirect('login')
    else:
        messages.error(request, 'User activation failed')
        return redirect('login')


def resend_activation(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            if not user.is_active:
                activate_user = ActivateUser.objects.get(user=user)
                send_mail(
                    subject='Reactivate your account for URL Shortener',
                    message=f'Click the link to reactivate your account: {settings.DOMAIN}/activate/{activate_user.token}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user.email],
                    fail_silently=False
                )
                messages.success(request, f'Reactivation email sent to {user.email}')
            else:
                messages.error(request, 'User is already active.')
        else:
            messages.error(request, 'User with this email does not exist.')

        return redirect('login')  # Redirect to login page or wherever you want

    return render(request, 'users/resend_activation.html')


def logout_user(request):
    logout(request)
    return redirect('login')
