from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.AllStudiosView.as_view(), name='studios_list'),
    path('<int:pk>/',views.StudioView.as_view(), name='studio_detail'),
    path('new',views.studio_new, name='studio_new'),
    path('edit/<int:pk>', views.studio_edit, name='studio_edit'),
]
