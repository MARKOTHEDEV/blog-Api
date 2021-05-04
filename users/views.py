# from rest_framework.viewsets import ModelViewSet,ViewSetMixin
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework.authtoken.views import ObtainAuthToken
from . import serializer
from rest_framework.renderers import api_settings
from rest_framework import permissions,authentication
from . import permissions as mypermissions
from rest_framework.decorators import action


class CreateUser(GenericViewSet,mixins.CreateModelMixin):
    serializer_class = serializer.CreateUserSerializer




class LoginUser(ObtainAuthToken):
    serializer_class =serializer.LoginSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class ProfileViewSet(ModelViewSet):
    serializer_class = serializer.UserProfileSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (permissions.IsAuthenticated,mypermissions.IsOWner,)
    authentication_classes = (authentication.TokenAuthentication,)


    def upload_image(self):
        pass

