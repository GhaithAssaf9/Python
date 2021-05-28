from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('log_in', views.login),
    path('register', views.sign_up),
    path('log_out', views.logout),
    path('success', views.success)
    ]
