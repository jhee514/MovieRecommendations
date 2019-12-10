from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Movie, Review, Genre
from django.contrib.auth.decorators import login_required
from .forms import MovieModelForm, ReviewModelForm

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html',{
        'movies':movies,
    })

@require_GET
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id = movie_id)
    reviews = movie.review_set.all()
    review_form = ReviewModelForm()
    return render(request, 'movies/movie_detail.html', {
        'movie':movie,  
        'reviews':reviews,
        'review_form':review_form,
    })

@require_POST
@login_required
def reviews_new(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    form = ReviewModelForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.movie = movie
        review.save()
    return redirect('movies:movie_detail', movie_id)
    
@login_required
def reviews_delete(request, movie_id, reviews_id):
    movie = get_object_or_404(Movie, movie_id)
    review = get_object_or_404(Review, review_id)
    if request.user == review.user: 
        review.delete()
        return redirect('movies:movie_detail', movie_id)

@login_required
def like(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    user = request.user
    # if article.like_users.filter(id=user.id).exists():
    if user in movie.like_users.all():  # 이미 좋아요 상태
        movie.like_users.remove(user)   # 고로 지움
    else:
        movie.like_users.add(user)
    return redirect('movies:movie_detail', movie_id)
