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
