from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('log_in', views.login),
    path('register', views.sign_up),
    path('log_out', views.logout),
    path('wall', views.success),
    path('add_post', views.add_post),
    path('add_comment/<int:m_id>', views.add_comment),
    # path('view_comments/<int:p_id>', views.view_comments),
    path('delete_p/<int:pp_id>', views.delete_post),
    path('delete_c/<int:cc_id>', views.delete_comment),
    ]
