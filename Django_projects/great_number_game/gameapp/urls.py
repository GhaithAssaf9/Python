from django.urls import path
from . import views
urlpatterns = [
    path('', views.game),
    path('submitt', views.result),
    path('again', views.playagain)
]