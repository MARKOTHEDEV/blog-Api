from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model


# Create your models here.



class Blog(models.Model):

    authorChoice = (
        ('Politics','Politics'),
        ('Entertainment','Entertainment'),
        ('Travel','Travel'),
        ('Sports','Sports'),
        ('Tech','Tech'),
    )
    category = models.CharField(choices=authorChoice,max_length=500,blank=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    blogPost = models.TextField()
    blogPost2 = models.TextField(blank=True)

    introPics = models.ImageField(upload_to='blog/%d/',null=True)
    contentHeader = models.ImageField(upload_to='blog/%d/',null=True)
    extrapics = models.ImageField(upload_to='blog/%d/',null=True)

    dateCreated = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return f'{self.author} ----> {self.title}'

    @property
    def authorName(self):
        'this returns the actual name of the author unlike the self.author that returns the id of the user model'
        name = get_user_model().objects.get(id=self.author.id)
        return name.email

    @property
    def authorImage(self):
        'this returns the actual image of the author'
        name = get_user_model().objects.get(id=self.author.id)
        return name.image.url

    @property
    def introContent(self):
        'this what u see before u click on read more..'
        return f'{self.blogPost[0:30]}....'



class Comment(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment = models.TextField()



    def __str__(self):
        return f'{self.user} commented on {self.blog}'

    @property
    def commenterimage(self):
        'this return the image of the person that creates a comment instance'
        return self.user.image.url

    @property
    def commenterName(self):
        return self.user.name
