from rest_framework.routers import DefaultRouter,SimpleRouter
from . import views
from django.urls import path,include
route = DefaultRouter()
route2 = DefaultRouter()



route.register('blog',views.BlogViewSet)
route2.register('',views.CommentViewset)

urlpatterns = [
    path('',include(route.urls)),
    path('comment/',include(route2.urls)),

]