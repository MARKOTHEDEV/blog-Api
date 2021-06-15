from django.http import request
from django.shortcuts import render

# Create your views here.





def index(request,pk=None):
    'This view displays the index page the where all the blog post is located'

    return render(request,'index.html')


def blogDetail(request,pk=None):
    'this view renders the blog-detail markup'
    context = {'pk':pk}
    return render(request,'single.html',context)


def blogcategories(request,category=None):
    'this reders the blog categories'
    context = {'category':category}
    return render(request,'category.html',context)




def createPost(request):
    return render(request,'createUser.html')
def updatePost(request,pk=None):
    'this view renders the blog-Update markup'
    context = {'pk':pk}

    return render(request,'updatePost.html',context)


def create_account(request):
    return render(request,'signup.html')


def user_login(request):
    return render(request,'login.html')


def profilePage(request):
    return render(request,'profile.html')


def forgotPasswordPage(request):
    return render(request,'forgot-password.html')

def passwordConfirm(request):
    "this template tells the user that the email has been sent"
    return render(request,'password-reset-confirm.html')
