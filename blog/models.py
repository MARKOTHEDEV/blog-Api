from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class PostType(models.Model):
    'this model let the blog website so in feature we can add more blog post'
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Blog(models.Model):

    postType = models.ForeignKey(PostType,on_delete=models.SET_NULL,null=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    blogPost = models.TextField()

    def __str__(self):
        return f'{self.author} ----> {self.title}'




class Comment(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f'{self.user} commented on {self.blog}'