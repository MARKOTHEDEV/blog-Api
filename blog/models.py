from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.



class Blog(models.Model):

    authorChoice = (
        ('Politics','Politics'),
        ('Tech','Tech'),
        ('Entertainment','Entertainment'),
        ('Travel','Travel'),
        ('Sports','Sports'),
    )
    category = models.CharField(choices=authorChoice,max_length=500,blank=True)
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