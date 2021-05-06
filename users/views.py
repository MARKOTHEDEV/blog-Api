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
from rest_framework.response import Response

class CreateUser(GenericViewSet,mixins.CreateModelMixin):
    serializer_class = serializer.CreateUserSerializer




class LoginUser(ObtainAuthToken):
    serializer_class =serializer.LoginSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class ProfileViewSet(ModelViewSet):
    'this view can update and get a list of all the user to update u should use patch--for your javascript'
    serializer_class = serializer.UserProfileSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (permissions.IsAuthenticated,mypermissions.IsOWner,)
    authentication_classes = (authentication.TokenAuthentication,)


    def get_serializer_class(self):
        if self.action == 'upload_imageAction':
            return serializer.UserProfileImageSerializer
        
        return self.serializer_class

    # def update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return super().update(request, *args, **kwargs)



    @action(detail=True,methods=['post',],url_path='upload_image')
    def upload_imageAction(self, request, pk=None):
        user = self.get_object()
        print(request.data)
        imageserialzer = serializer.UserProfileImageSerializer(user,data=request.data)
        if imageserialzer.is_valid():
            imageserialzer.save()

        return Response(imageserialzer.data)