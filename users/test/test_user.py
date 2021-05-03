from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model


CREATE_USER = reverse('user_profile-list')



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