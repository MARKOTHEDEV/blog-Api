from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register('',views.CreateUser,basename='user_profile')



urlpatterns = [
    path('create-user/',include(route.urls)),
    path('login/',views.LoginUser.as_view(),name='user_login')
]

