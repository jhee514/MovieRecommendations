from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_id>',views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/reviews/new', views.reviews_new, name='reviews_new'),
    path('<int:movie_id>/reviews/delete', views.reviews_delete, name='reviews_delete'),
    path('<int:movie_id>/like', views.like, name='like'),
]
