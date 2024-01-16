from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from dashboard.models import Url

# Create your views here.


@login_required
def dashboard(request):
    user_urls = Url.objects.filter(user=request.user)
    return render(request, 'dashboard/dashboard.html', {'user_urls': user_urls})


@login_required
def create_url(request):
    domain = settings.DOMAIN
    if request.method == "POST":
        url = request.POST['url']
        short_url = request.POST['shorten']

        if url.strip() == '' or short_url.strip() == '':
            messages.error(request, 'All fields are required')
            return redirect('create-url')

        if "https://" not in url and "http://" not in url:
            url = "https://" + url

        if Url.objects.filter(short_url=short_url).exists():
            messages.error(request, 'Short url already exists')
            return redirect('create-url')
        else:
            url = Url.objects.create(
                user=request.user,
                url=url,
                short_url=short_url
            )
            url.save()
            messages.success(request, 'Url created successfully')
            return redirect('dashboard')

    return render(request, 'dashboard/create_url.html', {'domain': domain})


@login_required
def delete_url(request, _id):
    if request.method == "POST":
        url = get_object_or_404(Url, id=_id)
        if url.user == request.user:
            url.delete()
            messages.success(request, 'Url deleted successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'You are not authorized to delete this url')
            return PermissionDenied


def redirect_url(request, short_url):
    url_object = get_object_or_404(Url, short_url=short_url)
    if url_object.url is not None:
        url_object.clicks += 1
        url_object.save()
        return redirect(url_object.url)
