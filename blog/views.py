from blog import models as blog_models
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from . import permissions as custompermissions
from . import serializer as myserializers



class BlogViewSet(ModelViewSet):
    queryset = blog_models.Blog.objects.all()
    serializer_class = myserializers.BlogSerializer
    permission_classes  = (custompermissions.AllOwnerToEdit,)
    authentication_classes = (TokenAuthentication,)


    def perform_create(self,serializer):
        serializer.save(author =self.request.user)