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

    @action(methods=['GET'],detail=True,url_path='filterbycategory')
    def filter_by_categories(self, request, pk=None):
        'this view renders data based on the categorie that was inputed'
        # self.kwargs.get('pk') in the sense doesnt mean primry key it the categorie that was parsed into the url
        filted_dataBlogPost = blog_models.Blog.objects.filter(category__icontains=self.kwargs.get('pk'))
        newSerializedData = self.serializer_class(filted_dataBlogPost,many=True)
        return Response(newSerializedData.data)



    def perform_create(self,serializer):

        '''this function is used to assign a Blog post that was juscreated to a author 
                So it done automatically since we wrote our serializer i a way that he login in user can't assign a author
                

                Any body that create a blog post when he is logged in he becomes the autor of he post!
        '''
        serializer.save(author=self.request.user)


    
    
    
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

        return Response(serializedData.data)