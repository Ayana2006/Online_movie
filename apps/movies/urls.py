from django.urls import path
from apps.movies.views import movie_detail, movie_catalog, series, search
urlpatterns = [
    path('<int:id>/', movie_detail, name = 'movie_detail'),
    path('movie_catalog/<slug:slug>/', movie_catalog, name='movie_catalog'),
    path('series/<int:id>/', series, name='series'),
    path('search/', search, name='search'),
]

 