from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from  blog import models
from rest_framework import status

def create_user(**kwargs):
    'this function helps us create a user it jus an helper function that prevent us from writing reated code'

    return get_user_model().objects.create_user(**kwargs)

CREATE_POST_URL  = reverse('blog-list')



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