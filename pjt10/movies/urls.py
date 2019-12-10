from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies_list, name='movies_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/review/new/>', views.create_review, name='create_review'),
    path('<int:movie_id>/review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('<int:movie_id>/like/', views.like_movie, name='like_movie'),
]
