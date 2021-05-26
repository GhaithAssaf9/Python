from django.urls import path     
from . import views
urlpatterns = [
    path('', views.main_page),
    path('shows', views.all_shows),
    path('shows/<int:num>', views.show_this_show),
    path('shows/<int:num>/edit', views.edit),
    path('delete/<int:num>', views.delete),
    path('shows/new', views.add_new)
    ]
