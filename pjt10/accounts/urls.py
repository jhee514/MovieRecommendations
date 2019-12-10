from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('follow/<int:user_id>/', views.follow, name='follow'),

    path('<int:user_id>/', views.user_page, name='user_page'),
]

