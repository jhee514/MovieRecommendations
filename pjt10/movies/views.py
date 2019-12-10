from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.contrib.auth.decorators import login_required
from .models import Movie, Genre, Reviews
from .forms import ReviewsModelForm


def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/list.html', {
        'movies': movies
    })


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews_set.all()
    review_form = ReviewsModelForm()
    return render(request, 'movies/detail.html', {
        'movie': movie,
        'reviews': reviews,
        'review_form': review_form
    })


@login_required
@require_POST
def create_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        review_form = ReviewsModelForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect(movie)
    return redirect('movies:movies_list')


@login_required
@require_POST
def delete_review(request, movie_id, review_id):
    review = get_object_or_404(Reviews, id= review_id)
    if review.user == request.user:
        review.delete()
    return redirect('movies:movie_detail', movie_id)


@login_required
def like_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    user = request.user
    if movie.like_user.filter(id=user.id).exists():
        movie.like_user.remove(user)
    else:
        movie.like_user.add(user)
    return redirect(movie)

    