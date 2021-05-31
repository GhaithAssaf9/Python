from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('log_in', views.login),
    path('register', views.sign_up),
    path('log_out', views.logout),
    path('wall', views.success),
    path('add_post', views.add_post),
    path('delete_p/<int:pp_id>', views.delete_post),
    path('details/<int:id>', views.details),
    path('like/<int:id>', views.like),
    path('dislike/<int:id>', views.dislike),
    path('success', views.success),
    ]
