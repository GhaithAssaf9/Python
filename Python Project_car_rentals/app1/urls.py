from django.urls import path
from.import views
urlpatterns = [
    path('', views.home),
    path('login', views.login_register),
    path('logout', views.log_out),
    path('signin', views.log),
    path('gallery', views.gallery),
    path('book', views.book),
    path('add_car', views.add_car),
    path('carrr', views.carrr),
    path('micro', views.micro),
    path('suv', views.suv),
    path('luxury', views.luxury),
    path('sedan', views.sedan),
    path('account', views.account),
    path('details/<int:id>', views.details),
    path('reserve/<int:id>', views.reservation),
    path('thanks/<int:id>', views.thanks),
    path('about', views.about),
    ]