from django.urls import path
from . import views
urlpatterns = [
    path('', views.first),
    path('ggg', views.goldcc),
    path('reset', views.reset),
    ]