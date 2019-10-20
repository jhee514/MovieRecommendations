from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from .models import Movie, Review
from .forms import MovieModelForm, ReviewModelForm

@require_GET
def index(request):
    movies = Movie.objects.all()
    return render(request, 'cinema/index.html', {
        'movies':movies,
    })

@require_GET
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'cinema/movie_list.html', {
        'movies':movies,
    })

@require_http_methods(['GET', 'POST'])
def create_movie(request):
    if request.method =='POST':
        form = MovieModelForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect(movie)
    else:
        form = MovieModelForm()
    return render(request, 'cinema/create_movie.html', {
        'form': form,
    })

@require_GET
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.review_set.all()
    review_form = ReviewModelForm()
    return render(request, 'cinema/movie_detail.html', {
        'movie':movie,
        'reviews':reviews,
        'review_form':review_form,
    })

@require_http_methods(['GET', 'POST'])
def update_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect(movie)
    else:
        form = MovieModelForm(instance=movie)
    return render(request, 'cinema/update_movie.html', {
        'form':form,
    })

@require_POST
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('cinema:movie_list')

@require_http_methods(["GET", "POST"])
def create_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)   
    form = ReviewModelForm(request.POST)
    review = form.save(commit=False)
    review.movie = movie
    review.save()
    return redirect(movie)

@require_POST
def delete_review(request, movie_id, review_id):
    movie = get_object_or_404(Movie, id=movie_id)
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return redirect(movie)

