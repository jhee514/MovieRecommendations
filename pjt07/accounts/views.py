from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.contrib.auth import login as auth_login, logout as auth_log_out
from django.contrib.auth.decorators import login_required

from .forms import CustomAuthenticationForm, CustomUserCreationForm

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
        return redirect('/')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect(user)
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form, 
    })

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:movie_list')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:movie_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
    })

@login_required
def logout(request):
    if request.user.is_authenticated:
        auth_log_out(request)
    return redirect('movies:movie_list')

@login_required
def user_page(request, user_id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=user_id)
        return render(request, 'accounts/detail.html', {
            'user_info': user,
        })
    return redirect('movies:movie_list')