from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, UserSiteForm
from django.contrib.auth.decorators import login_required
from .models import UserSite, SiteVisit
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
import requests
import time
from django.utils.timezone import now


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш акаунт створено, {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'vpn/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ваш профіль оновлено!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user.profile)

    return render(request, 'vpn/profile.html', {'form': form})


def home(request):
    return render(request, 'vpn/home.html')


@login_required
def add_site(request):
    if request.method == 'POST':
        form = UserSiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.user = request.user
            site.save()
            messages.success(request, 'Сайт успішно додано!')
            return redirect('sites')
    else:
        form = UserSiteForm()
    return render(request, 'vpn/add_site.html', {'form': form})


@login_required
def user_sites(request):
    sites = UserSite.objects.filter(user=request.user)
    return render(request, 'vpn/user_sites.html', {'sites': sites})


@login_required
def proxy(request, site_id):
    site = get_object_or_404(UserSite, id=site_id, user=request.user)
    url = site.url + request.path_info[len(f'/sites/{site_id}/'):]
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text
        content = content.replace(site.url, request.build_absolute_uri(f'/sites/{site_id}/'))

        SiteVisit.objects.create(
            user=request.user,
            site=site,
            data_sent=len(request.body),
            data_received=len(response.content),
            timestamp=now()
        )
        return HttpResponse(content, content_type=response.headers['Content-Type'])
    else:
        return HttpResponseNotFound('Сайт не знайдено')


@login_required
def statistics(request):
    visits = SiteVisit.objects.filter(user=request.user)
    return render(request, 'vpn/statistics.html', {'visits': visits})
