from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.



class MyuserManager(BaseUserManager):
    'this class handles the management of the Myuser class'
    def create_user(self,name,email,password=None):
        'this function helps create a userInstance using Myuser Model'
        email = self.normalize_email(email)
        user = self.model(name=name,email=email)
        user.set_password(password)
        
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,password=None):
        'when we call the create_user it returns a newly created instance all we need to do is to attach so permiisions to it'
        user = self.create_user(email=email,name='Superuser',password=password)
        user.is_staff = True
        user.is_superuser =True
        user.save(using=self._db)

        return user


class Myuser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='userImage/%d/',default='user.jpg')
    bio = models.TextField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # so instead of using name to login we use email and password
    USERNAME_FIELD = 'email'



    # this tells django how to mamange our Myuser model
    objects = MyuserManager()

    def __str__(self):
        return self.name or self.email



