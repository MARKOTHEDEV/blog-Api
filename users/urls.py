from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()


router.register('create-user',views.CreateUser,basename='create-user')
router.register('myprofile',views.ProfileViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('login/',views.LoginUser.as_view(),name='user_login'),

]

