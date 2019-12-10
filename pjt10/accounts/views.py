from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.contrib.auth import login as auth_login, logout as auth_log_out
from django.contrib.auth.decorators import login_required

from .forms import CustomAuthenticationForm, CustomUserCreationForm
from movies.models import Reviews

from django.contrib.auth import get_user_model
User = get_user_model()

def index(request):
    users = User.objects.all()
    return render(request, 'accounts/index.html', {
        'users': users,
    })

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form, 
    })


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:movies_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
    })


@login_required
def logout(request):
    if request.user.is_authenticated:
        auth_log_out(request)
    return redirect('movies:movies_list')


@login_required
@require_GET
def user_page(request, user_id):
    if request.user.is_authenticated:
        user = request.user
        detail_user = get_object_or_404(User, id=user_id)
        fans = detail_user.fans.all().count()
        stars = detail_user.star.all().count()
        is_like = detail_user.fans.filter(id=user.id).exists()
        reviews = Reviews.objects.filter(user=detail_user)
        return render(request, 'accounts/detail.html', {
            'user_info': detail_user,
            'fans': fans,
            'stars': stars,
            'is_like': is_like,
            'reviews': reviews,
        })
    return redirect('movies:movies_list')

@login_required
@require_POST
def follow(request, user_id):
    fan = request.user
    star = get_object_or_404(User, id=user_id)
    if fan != star:
        if star.fans.filter(id=fan.id).exists():
            star.fans.remove(fan)
        else:
            star.fans.add(fan)
    return redirect(star)