from blog import models as blog_models
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from . import permissions as custompermissions
from . import serializer as myserializers
from rest_framework.response import Response


class BlogViewSet(ModelViewSet):
    queryset = blog_models.Blog.objects.all()
    serializer_class = myserializers.BlogSerializer
    permission_classes  = (custompermissions.AllOwnerToEdit,permissions.IsAuthenticatedOrReadOnly)
    authentication_classes = (TokenAuthentication,)


    def perform_create(self,serializer):
        serializer.save(author=self.request.user)

        # try:
        #     serializer.save(author=self.request.user)
        # except ValueError:
        #     raise ValueError('This user Is AnonymousUser So Creating Blog is not Allowed')

    
class CommentViewset(ModelViewSet):
    queryset = blog_models.Comment.objects.all()
    serializer_class = myserializers.CommentSerializer
    permission_classes  = (permissions.IsAuthenticatedOrReadOnly,custompermissions.AllowOwnerToEditComment)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


    def retrieve(self,request,**kwargs):
        'based on the blog we have opened we can see it own comment'
        '/api/blog/comment/1/ -- u must specify the blog id to getit comment'
        allComment = self.queryset.filter(blog=kwargs.get('pk'))
        
        serializedData = self.serializer_class(allComment,many=True)

        return Response([serializedData.data])