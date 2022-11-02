from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('<int:pk>/', views.post_detail, name="detail"),
    path('user_post/', views.user_post, name="user_post"),
]
