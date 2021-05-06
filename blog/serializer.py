from rest_framework import serializers

from blog import models as blog_models


class BlogSerializer(serializers.ModelSerializer):
    """handles serializing data for blogviewset"""

    class Meta:
        """Meta definition for serializers."""

        model = blog_models.Blog
        fields = ('id','title','blogPost','postType','author')
        read_only = ['author','id']
