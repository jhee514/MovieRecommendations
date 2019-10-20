from django.urls import path
from . import views

app_name = 'cinema'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('create/', views.create_movie, name='create_movie'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/edit/', views.edit_movie, name='edit_movie'),
    path('<int:movie_id>/delete/', views.delete_movie, name='delete_movie'),
]
