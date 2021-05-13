from django.db.models import fields
from rest_framework import serializers

from blog import models as blog_models
import blog


class BlogSerializer(serializers.ModelSerializer):
    """handles serializing data for blogviewset"""

    class Meta:
        """Meta definition for serializers."""

        model = blog_models.Blog
        fields = ('id','title','blogPost','category','author','contentHeader','introPics')
        # read_only = ['id']
        extra_kwargs={
            'id':{'read_only':True},
            'author':{'read_only':True},
            # 'contentHeader':{'read_only':True},
            # 'introPics':{'read_only':True},
        }


class BlogImageSerializer(serializers.ModelSerializer):
    "this serializer handles the images that are associated withe blog"

    class Meta:
        model = blog_models.Blog
        fields  = ('contentHeader','introPics')

        

class CommentSerializer(serializers.ModelSerializer):




    class Meta:
        """Meta definition for serializers."""

        model = blog_models.Comment
        fields = ('id','blog','user','comment')
        # read_only = ['id']
        extra_kwargs={
            'id':{'read_only':True},
            'user':{'read_only':True}
        }
