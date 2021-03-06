from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name='list-of-all-blogpost'),
    path('blog-detail/<int:pk>/',views.blogDetail,name='blog-detail'),
    path('update-blog/<int:pk>/',views.updatePost,name='update-blog'),
    path('create-acct/',views.create_account,name='create-acct'),
    path('login/',views.user_login,name='frontend_login'),
    path('create-post/',views.createPost,name='createPost'),
    path('blog-categories/<str:category>/',views.blogcategories,name='blogcategories'),
    path('profile/',views.profilePage,name='profile-page'),
    path('forgot-password/',views.forgotPasswordPage,name='forgotPasswordPage'),
    path('passwordConfirm/',views.passwordConfirm,name='passwordConfirm')
]