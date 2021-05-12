from rest_framework import serializers

from blog import models as blog_models


class BlogSerializer(serializers.ModelSerializer):
    """handles serializing data for blogviewset"""

    class Meta:
        """Meta definition for serializers."""

        model = blog_models.Blog
        fields = ('id','title','blogPost','category','author')
        # read_only = ['id']
        extra_kwargs={
            'id':{'read_only':True},
            'author':{'read_only':True}
        }


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
