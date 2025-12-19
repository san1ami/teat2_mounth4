from django.urls import path
from .views import MovieListView
from .views import (
    MovieListView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
    movie_search,
    movies_by_genre,
)

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('add/', MovieCreateView.as_view(), name='movie_add'),
    path('edit/<int:pk>/', MovieUpdateView.as_view(), name='movie_edit'),
    path('delete/<int:pk>/', MovieDeleteView.as_view(), name='movie_delete'),
    path('search/', movie_search, name='movie_search'),
    path('genre/<int:genre_id>/', movies_by_genre, name='movies_by_genre'),
]
