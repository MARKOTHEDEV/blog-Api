# from rest_framework.viewsets import ModelViewSet,ViewSetMixin
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework.authtoken.views import ObtainAuthToken
from . import serializer
from rest_framework.renderers import api_settings


class CreateUser(GenericViewSet,mixins.CreateModelMixin):
    serializer_class = serializer.CreateUserSerializer




class LoginUser(ObtainAuthToken):
    serializer_class =serializer.LoginSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

