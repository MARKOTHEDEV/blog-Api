from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from  blog import models
from rest_framework import status

def create_user(**kwargs):
    'this function helps us create a user it jus an helper function that prevent us from writing reated code'

    return get_user_model().objects.create_user(**kwargs)

def create_blogpost(**params):
    'helper funtion that create a blog post on call of it'
    return models.Blog.objects.create(**params)

CREATE_POST_URL  = reverse('blog-list')

def update_post_url(id):
    return reverse('blog-detail',args=[id,])


class TestBlogAuthUser(TestCase):
    'this test is for auth users'

    def setUp(self):
        self.client = APIClient()
        paylaod = {'name':'matthew','email':'marko2@gmail.com','password':'YouCrazyWIthProgramming'}
        self.user = create_user(**paylaod)
        self.client.force_authenticate(self.user)

    def test_user_create_blog(self):
        blogpost = {'title':'heloo world','blogPost':'thedhbfdbfrd'}
        resp = self.client.post(CREATE_POST_URL,blogpost)



        self.assertEqual(resp.status_code,status.HTTP_201_CREATED)
        isBlogExits = models.Blog.objects.filter(author=self.user,title=resp.data.get('title'))
        self.assertTrue(isBlogExits)




    def test_partial_upate_blog_post(self):
        blogpost = {'title':'heloo world','blogPost':'thedhbfdbfrd'}
        # create_blogpost(**blogpost)
        # we have created the blog so now let try to update it
        createBlogResp =   self.client.post(CREATE_POST_URL,blogpost)
        resp = self.client.patch(update_post_url(createBlogResp.data.get('id')),{'title':'Yo(Updated by marko)'})


        self.assertEqual(resp.status_code,status.HTTP_200_OK)
        self.assertEqual(resp.data.get('title'),'Yo(Updated by marko)')


    def test_delete_post(self):
        'this post helps test deletion of post'
        # first we need to create a post with a logged in user
        blogpost = {'title':'heloo world','blogPost':'thedhbfdbfrd'}
        # we have to test if it was created first
        createBlogResp =   self.client.post(CREATE_POST_URL,blogpost)
        self.assertEqual(createBlogResp.status_code,status.HTTP_201_CREATED)
        # let check if the post was created
        self.assertTrue(models.Blog.objects.filter(id=createBlogResp.data.get('id')).exists())
        # we have created the blog so now let try to delete the BlogPost it

        # dont be confused! 
        # the 
        # update_post_url is the same as a detail view that accept an id to identify the object
        #  we want to perform task on
        deleteBlogPostresp = self.client.delete(update_post_url(createBlogResp.data.get('id')))
        
        self.assertEqual(deleteBlogPostresp.status_code,status.HTTP_204_NO_CONTENT)
        self.assertFalse(models.Blog.objects.filter(id=createBlogResp.data.get('id')).exists())



class TestUnAuthBlogUSer(TestCase):
    'this class test the un auth users=>on how they use the blog'

    def setUp(self):
        self.client = APIClient()



    def test_unAuth_user_create_blogPost(self):
        blogpost = {'title':'heloo world','blogPost':'thedhbfdbfrd'}
        resp = self.client.post(CREATE_POST_URL,blogpost)
        payload = {'name':'matthew','email':'marko2@gmail.com','password':'YouCrazyWIthProgramming'}
        user = create_user(**payload)


        self.assertEqual(resp.status_code,status.HTTP_401_UNAUTHORIZED)
        isBlogExits = models.Blog.objects.filter(author=user,title=resp.data.get('title'))
        self.assertFalse(isBlogExits)

    