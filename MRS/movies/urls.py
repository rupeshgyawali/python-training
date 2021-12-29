from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>', views.details, name='details'),
    # path('top-movies/', views.top_movies, name='top-movies'),
    # path('top-series/', views.top_series, name='top-series'),
]