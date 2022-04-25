from django.urls import path, include
from post.views import *

urlpatterns = [
    path('list/', post_list, name='post_list'),
    path('title/list/', post_title_list, name='post_title_list'),
    path('detail/<pk>', post_detail, name='post_detail'),
]
