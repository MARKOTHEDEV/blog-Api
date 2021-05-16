from blog import models as blog_models
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions, serializers
from . import permissions as custompermissions
from . import serializer as myserializers
from rest_framework.response import Response



class BlogViewSet(ModelViewSet):
    queryset = blog_models.Blog.objects.all()
    serializer_class = myserializers.BlogSerializer
    permission_classes  = (permissions.IsAuthenticatedOrReadOnly,custompermissions.AllowAuthorToEditPost,)
    authentication_classes = (TokenAuthentication,)
    
    # pagination_class = 


    def perform_create(self,serializer):

        '''this function is used to assign a Blog post that was juscreated to a author 
                So it done automatically since we wrote our serializer i a way that he login in user can't assign a author
                

                Any body that create a blog post when he is logged in he becomes the autor of he post!
        '''
        serializer.save(author=self.request.user)

    # def get_serializer_class(self):
    #     if self.action == 'upload_pics':
    #         # print('heloo world')
    #         return myserializers.BlogImageSerializer

    #     return super().get_serializer_class()

  

    
    
    
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

        return Response([serializedData.data],status=serializedData.status)