from django.urls import path, include

from . import views

app_name = 'api'

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('categoria', views.CategoriaView.as_view()),
    path('post', views.PostView.as_view()),
    path('categoria/<int:pk>/', views.CategoriaDetailView.as_view()),
    path('post/<int:pk>/', views.PostDetailView.as_view()),
]