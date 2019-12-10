# Project06

## Goal



## Prerequisite

1.  startproject

2.  startapp

3.  settings.py

    1.  INATALLED_APPS

4.  urls.py

    1.  url_patterns

    

## Code



### models.py

-   ```python
    from django.db import models
    from django.urls import reverse
    
    class Movie(models.Model):
        title = models.CharField(max_length=200)
        title_en = models.CharField(max_length=200)
        audience = models.IntegerField()
        open_data = models.DateField(auto_now=False, auto_now_add=False)
        genre = models.CharField(max_length=100)
        watch_grade = models.CharField(max_length=50)
        score = models.FloatField()
        poster_url = models.TextField()
        description = models.TextField()
    
        def get_absolute_url(self):
            return reverse("cinema:movie_detail", kwargs={"movie_id": self.id})
        
    
    class Review(models.Model):
        content = models.CharField(max_length=300)
        score = models.IntegerField()
        created_at = models.DateTimeField(auto_now_add=True)
        movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    ```

    -   명세에 나와 있는 항목 대로 ``Movie`` 와 ``Review`` model 을 작성하였다.



### forms.py

-   ```python
    from django import forms
    from .models import Movie, Review
    
    class MovieModelForm(forms.ModelForm):
        class Meta():
            model = Movie
            fields = '__all__'
    
    class ReviewModelForm(forms.ModelForm):
        class Meta():
            model = Review
            fields = ('content', 'score', )
    ```

-   위에서 생성한 Model 의 입력을 편하게 바디 위하여 form을 작성하였다.

-   이 때, Review Model 의 경우는 'content', 와 'score' 항목만 입력을 받을 것이기 때문에 ``fields`` 를 따로 설정해 준다.



### urls.py

-   ```python
    from django.contrib import admin
    from django.urls import path
    
    from . import views
    
    app_name = 'cinema'
    
    urlpatterns = [
        path('', views.index, name='index'),
        path('list/', views.movie_list, name='movie_list'),
        path('create/', views.create_movie, name='create_movie'),
        path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
        path('<int:movie_id>/update/', views.update_movie, name='update_movie'),
        path('<int:movie_id>/delete/', views.delete_movie, name='delete_movie'),
        path('<int:movie_id>/create_review/', views.create_review, name='create_review'),
        path('<int:movie_id>/delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    ]
    ```

-   

### views.py

-   ```python
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
    ```

-   

### Screenshot



![screenshtot_01](.\images\screenshtot_01.png)

![screenshtot_02](.\images\screenshtot_02.png)

![screenshtot_03](.\images\screenshtot_03.png)

![screenshtot_04](.\images\screenshtot_04.png)

![screenshtot_05](.\images\screenshtot_05.png)

![screenshtot_07](.\images\screenshtot_06.png)

![screenshtot_08](.\images\screenshtot_08.png)

![screenshtot_09](.\images\screenshtot_09.png)



## Author

-   김지희 @jhee514



