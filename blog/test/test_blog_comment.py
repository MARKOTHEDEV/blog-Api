from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from blog import models as blog_models

CREATE_COMMENT_URL = reverse('comment-list')

def comment_url_with_argument(pk):
    return reverse('comment-detail',args=[pk,])

def create_blogpost(**params):
    'helper funtion that create a blog post on call of it'
    return blog_models.Blog.objects.create(**params)

def create_user(**kwargs):
    'this function helps us create a user it jus an helper function that prevent us from writing reated code'

    return get_user_model().objects.create_user(**kwargs)


# /api/blog/comment/    


class TestPublicComment(TestCase):
    'this class test the comment u dont need to be a login or created user to access this info u can be anybody'

    def setUp(self):
        self.client = APIClient()
        userPayload = {'name':'matthew','email':'marko5552@gmail.com','password':'Y8687ouCrazyWIthProgramming'}
        
        # we created a blog post her so we i wont repeat my self
        self.author = create_user(**userPayload)
        blogParams = {'author':self.author,'title':'jimmy Zang','blogPost':'Lorem ipsom'}
        self.blog = create_blogpost(**blogParams)




    def test_anyuserGet_Blog_comment(self):
        'this will Test getting all comment asociated with a particular Post'
        comment1 = blog_models.Comment.objects.create(user=self.author,blog=self.blog,comment="Yo nigga")
        comment2 = blog_models.Comment.objects.create(user=self.author,blog=self.blog,comment="Yo nigga by force")
        # now that we have two comment in the database it time to make GET request to the viewset
        # we are expecting to get two comment we created earlier

        resp = self.client.get(comment_url_with_argument(self.blog.id))

   
        # check if the our request was OK
        self.assertEqual(resp.status_code,status.HTTP_200_OK)
        # check if we got two comment we created earier
        self.assertEqual(len(resp.data),2)
        self.assertEqual(resp.data[0].get('id'),comment1.id)
        self.assertEqual(resp.data[1].get('id'),comment2.id)
      



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

    def test_if_auth_user_can_update_his_post(self):
        'this wil test if a login user can update his comment on a post'
        # first we need to create a blog post the author will be the self.user
        
        blogParams = {'author':self.user,'title':'jimmy Zang','blogPost':'Lorem ipsom'}
        blog = create_blogpost(**blogParams)
        # print(blog)

        # now we create another user and autheticate him so he can create a comment and update it
        userPayload = {'name':'matthew','email':'marko5552@gmail.com','password':'Y8687ouCrazyWIthProgramming'}
        newUser = create_user(**userPayload)
        self.client.force_authenticate(newUser)
        # so we send a post method the the create endpoint to create a comment
        comment_payload = {'comment':'The real seo is really good for testingn comment','blog':blog.id}
        Comment_resp = self.client.post(CREATE_COMMENT_URL,comment_payload)
        # we check if the comment was created
        self.assertEqual(Comment_resp.status_code,status.HTTP_201_CREATED)

        # since it was created we need to get the comment
        newUserComment = blog_models.Comment.objects.get(id=Comment_resp.data.get('id'))
        # now it time to test if we can update or  post
        comment_payloadUpdate = {'comment':'MARKOTHEDEV'}
        updateCommentResp = self.client.patch(comment_url_with_argument(newUserComment.id),comment_payloadUpdate)

        # print(updateCommentResp.data)
        # now we test if the newUSercomment was updated
        
        self.assertEqual(updateCommentResp.data.get('comment'),comment_payloadUpdate.get('comment'))


    def test_authUser_can_delete_comment(self):
        # first we create a Blog post we want to comment on
        blogParams = {'author':self.user,'title':'jimmy Zang','blogPost':'Lorem ipsom'}
        blog = create_blogpost(**blogParams)
        # next we created a new user who will comment on the Author:self.user post

        userPayload = {'name':'matthew','email':'marko5552@gmail.com','password':'Y8687ouCrazyWIthProgramming'}
        newUser = create_user(**userPayload)
        self.client.force_authenticate(newUser)
        # now we create aour comment
        comment_payload = {'comment':'The real seo is really good for testingn comment','blog':blog,'user':newUser} 
        comment = blog_models.Comment.objects.create(**comment_payload)

        # now it time to test if we can delete the comment
        resp = self.client.delete(comment_url_with_argument(comment.id))


        self.assertEqual(resp.status_code,status.HTTP_204_NO_CONTENT)
        # now let just test if the comment exits in our data base it must return false
        self.assertFalse(
            blog_models.Comment.objects.filter(id=comment.id).exists()
        )


class TestUnAuthUSer(TestCase):
    'this test all users that are not logged in also Known as Annoymous user'
    def setUp(self):
        self.client = APIClient()





    def test_if_unauthUser_can_create_comment(self):
        'this fucntion is to test the unauth user if they can delete comment'
        # we created a user first
        userPayload = {'name':'matthew','email':'marko5552@gmail.com','password':'Y8687ouCrazyWIthProgramming'}
        newUser = create_user(**userPayload)
        # self.client.force_authenticate(newUser)
        # assign that user to a blog post as it author
        blogParams = {'author':newUser,'title':'jimmy Zang','blogPost':'Lorem ipsom'}
        blog = create_blogpost(**blogParams)
        # next we created a new user who will comment on the Author:self.user post

        
        # then the unAuth user sends a post method the the create endpoint to create a comment
        comment_payload = {'comment':'The real seo is really good for testingn comment','blog':blog.id}
        Comment_resp = self.client.post(CREATE_COMMENT_URL,comment_payload)

        self.assertEqual(Comment_resp.status_code,status.HTTP_401_UNAUTHORIZED)


    def test_if_unauthUser_can_update_comment(self):
        'this fucntion is to test the unauth user if they can update comment'
        userPayload = {'name':'matthew','email':'marko5552@gmail.com','password':'Y8687ouCrazyWIthProgramming'}
        newUser = create_user(**userPayload)
        # self.client.force_authenticate(newUser)
        blogParams = {'author':newUser,'title':'jimmy Zang','blogPost':'Lorem ipsom'}
        blog = create_blogpost(**blogParams)
        # next we created a new user who will comment on the Author:self.user post

        
        # so we send a post method the the create endpoint to create a comment
        comment_payload = {'comment':'The real seo is really good for testingn comment(updated)'}
        Comment_resp = self.client.patch(CREATE_COMMENT_URL,comment_payload)
        # print(Comment_resp.data)
        self.assertEqual(Comment_resp.status_code,status.HTTP_401_UNAUTHORIZED)



    def test_if_unauthUser_can_delete_comment(self):
        'this fucntion is to test the unauth user if they can delete comment'
        userPayload = {'name':'matthew','email':'marko5552@gmail.com','password':'Y8687ouCrazyWIthProgramming'}
        newUser = create_user(**userPayload)
        # self.client.force_authenticate(newUser)
        blogParams = {'author':newUser,'title':'jimmy Zang','blogPost':'Lorem ipsom'}
        blog = create_blogpost(**blogParams)
        # next we created a new user who will comment on the Author:self.user post
        
        comment_payload = {'comment':'The real seo is really good for testingn comment','blog':blog,'user':newUser} 
        comment = blog_models.Comment.objects.create(**comment_payload)
        Comment_resp = self.client.delete(comment_url_with_argument(comment.id))
        # print(Comment_resp.data)
        self.assertEqual(Comment_resp.status_code,status.HTTP_401_UNAUTHORIZED)
