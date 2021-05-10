from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from blog import models as blog_models

CREATE_COMMENT_URL = reverse('comment-list')



def create_blogpost(**params):
    'helper funtion that create a blog post on call of it'
    return blog_models.Blog.objects.create(**params)

def create_user(**kwargs):
    'this function helps us create a user it jus an helper function that prevent us from writing reated code'

    return get_user_model().objects.create_user(**kwargs)



class TestAuthComment(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user =create_user(
            name='oge',
            email = 'lolwat@gmail.com',
            password = 'password123456'
        )
        self.client.force_authenticate(self.user)



    def test_if_auth_user_can_comment_on_a_post(self):
        'this test checks if any autheticatedd user can post on a blog post'
        # first we created a newUser who will be the one to comment on the post created by self.user
        userPayload = {'name':'matthew','email':'marko5552@gmail.com','password':'Y8687ouCrazyWIthProgramming'}
        newUser = create_user(**userPayload)

        blogParams = {'author':self.user,'title':'jimmy Zang','blogPost':'Lorem ipsom'}
        blog = create_blogpost(**blogParams)
        # print(blog)



        self.client.force_authenticate(newUser)
        comment_payload = {'comment':'The real seo is really good for testingn comment','blog':blog.id}
        resp = self.client.post(CREATE_COMMENT_URL,comment_payload)
        
        self.assertEqual(resp.status_code,status.HTTP_201_CREATED)
        self.assertEqual(resp.data.get('comment'),comment_payload.get('comment'))

        # we want to check if the comment that wasjust created was saved in the database
        isCommentExits = blog_models.Comment.objects.filter(id=resp.data.get('id'))
        self.assertTrue(isCommentExits)