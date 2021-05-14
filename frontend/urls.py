from django.urls import path
from . import views



urlpatterns = [
    path('',views.index),
    path('blog-detail/<int:pk>/',views.blogDetail,name='blog-detail'),
]