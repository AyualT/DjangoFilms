from django.urls import path
from . import views
from django.contrib.auth import views as acc_views

urlpatterns = [
    path(
        'change-password', 
        acc_views.PasswordChangeView.as_view(
            template_name = 'registration/change_pass.html',
            success_url = '/'
        ), 
        name='change_password'
    ),
    path('register/', views.create_user, name='register'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('get_moderator_status', views.get_moderator_status, name='get_mod'),
]
