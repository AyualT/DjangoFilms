from django.urls import path
from . import views

urlpatterns = [
    path('',views.AllFilmsView.as_view(), name='films_list'),
    path('film/<int:pk>',views.FilmView.as_view(), name='film_detail'),
    path('new',views.film_new, name='film_new'),
    path('edit/<int:pk>', views.film_edit, name='film_edit'),
    path('review/<int:fid>/<int:uid>', views.create_review, name='create_review'),
    path('reviewlike/<int:fid>/<int:rid>/<int:uid>/', views.like_review, name='like_review'),
    path('reviewdislike/<int:fid>/<int:rid>/<int:uid>/', views.dislike_review, name='dislike_review'),
    path('new_films/',views.NewFilmsView.as_view(), name='new_films_list'),
    path('popular_films/',views.PopularFilmsView.as_view(), name='popular_films_list'),
    path('films_by_rating/',views.RatingFilmsView.as_view(), name='films_by_rating_list'),
    path('action_films/',views.ActionFilmsView.as_view(), name='action_films_list'),
    path('comedy_films/',views.ComedyFilmsView.as_view(), name='comedy_films_list'),
    path('horror_films/',views.HorrorFilmsView.as_view(), name='horror_films_list'),
    path('thriller_films/',views.ThrillerFilmsView.as_view(), name='thriller_films_list'),
]
