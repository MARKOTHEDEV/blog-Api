# from rest_framework.viewsets import ModelViewSet,ViewSetMixin
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth import get_user_model
from rest_framework import mixins
from . import serializer



class CreateUser(GenericViewSet,mixins.CreateModelMixin):
    serializer_class = serializer.CreateUserSerializer
