from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path,include
route = DefaultRouter()
route.register('',views.BlogViewSet)

urlpatterns = [
    path('',include(route.urls)),
]