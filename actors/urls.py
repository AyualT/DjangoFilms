from django.urls import path
from . import views

urlpatterns = [
    path('',views.AllActorsView.as_view(), name='actors_list'),
    path('actor/<int:pk>',views.ActorView.as_view(), name='actor_detail'),
    path('new',views.actor_new, name='actor_new'),
    path('edit/<int:pk>', views.actor_edit, name='actor_edit'),
]
