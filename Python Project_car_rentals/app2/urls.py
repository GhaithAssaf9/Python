from django.urls import path
from.import views
urlpatterns = [
    # path('admin', views.main),
    path('', views.log),
    path('data', views.data),
    ]