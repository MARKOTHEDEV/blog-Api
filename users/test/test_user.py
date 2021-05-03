from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model


CREATE_USER = reverse('user_profile-list')
LOGIN_URL = reverse('user_login')

def create_user(**kwargs):
    'this function helps us create a user it jus an helper function that prevent us from writing reated code'

    return get_user_model().objects.create_user(**kwargs)


class TestAllUser(TestCase):
    'this class test the unauth user and authuser'

    def setUp(self):
        self.client = APIClient()


    def test_create_user(self):
        'this method create a user successfully'
        payload = {'name':'matthew','email':'marko2@gmail.com','password':'YouCrazyWIthProgramming'}
        resp = self.client.post(CREATE_USER,payload)

        user = get_user_model().objects.get(email=payload.get('email'))

        checkPassword = user.check_password(payload.get('password'))
  
        self.assertTrue(checkPassword)
        self.assertEqual(resp.status_code,status.HTTP_201_CREATED)

    def test_create_user_bad_input(self):
        'this is to test if the user when he/she input or post a empty data'

        resp = self.client.post(CREATE_USER,{}) 

        self.assertEqual(resp.status_code,status.HTTP_400_BAD_REQUEST)


    def test_create_user_with_short_password(self):
        'this function trys to create a user using a short password which is not allowed whilist the password should be 5 or above'
        payload = {'name':'matthew','email':'marko2@gmail.com','password':'You'}
        resp = self.client.post(CREATE_USER,payload)

        self.assertEqual(resp.status_code,status.HTTP_400_BAD_REQUEST)


    def test_authuser_login_successfully(self):
        'this test login a created user successfull'
        payload = {'name':'matthew','email':'marko2@gmail.com','password':'YouCrazyWIthProgramming'}
        # so this user was created successfully
        create_user(**payload)

        # now is time for the user to login with the right credentials
        # note this user is created already
        resp = self.client.post(LOGIN_URL,{'email':'marko2@gmail.com','password':'YouCrazyWIthProgramming'})

        self.assertEqual(resp.status_code,status.HTTP_200_OK)

    def test_authuser_login_with_bad_password(self):
        'this test login a created user with bad password'
        payload = {'name':'matthew','email':'marko2@gmail.com','password':'YouCrazyWIthProgramming'}
        # so this user was created successfully
        create_user(**payload)

        # now is time for the user to login with the right credentials
        # note this user is created already
        resp = self.client.post(LOGIN_URL,{'email':'marko2@gmail.com','password':'YouCeoeie8454e'})

        self.assertEqual(resp.status_code,status.HTTP_400_BAD_REQUEST)



class TestAuthUser(TestCase):

    def setUp(self):
        self.client = APIClient()
        payload = {'name':'matthew','email':'marko2@gmail.com','password':'YouCrazyWIthProgramming'}
        self.user = create_user(**payload)
        self.client.force_authenticate(self.user)


    