from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model


CREATE_USER = reverse('create-user-list')
LOGIN_URL = reverse('user_login')


def GET_USER_PROFILE(pk):
    'this is a url but it needs a parameter tha why i put it in a funtion'
    return reverse('myuser-detail',args=[pk])

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


    def test_unauthuser_login_with_bad_password(self):
        'this test login a created user with bad password'
 
        # now is time for the user to login with the right credentials
        # note this user is  not created 
        resp = self.client.post(LOGIN_URL,{'email':'marko2@gmail.com','password':'YouCeoeie8454e'})

        self.assertEqual(resp.status_code,status.HTTP_400_BAD_REQUEST)

    def test_unauthUser_retrevie_his_profile(self):
        'this function test the authuser it allows him to get his profile unsuccessfully'
        payload = {'name':'matthew','email':'marko2@gmail.com','password':'YouCrazyWIthProgramming'}
        user = create_user(**payload)
        # print(GET_USER_PROFILE(self.user.id))
        resp = self.client.get(GET_USER_PROFILE(user.id))

        self.assertEqual(resp.status_code,status.HTTP_401_UNAUTHORIZED)

class TestAuthUser(TestCase):

    def setUp(self):
        self.client = APIClient()
        payload = {'name':'matthew','email':'marko2@gmail.com','password':'YouCrazyWIthProgramming'}
        self.user = create_user(**payload)
        self.client.force_authenticate(self.user)


    def test_authUser_retrevie_his_profile(self):
        'this function test the authuser it allows him to get his profile successfully'
        # print(GET_USER_PROFILE(self.user.id))
        resp = self.client.get(GET_USER_PROFILE(self.user.id))

     
        self.assertEqual(resp.status_code,status.HTTP_200_OK)


    def  test_update_user_profile(self):
        'full updated'
        'this function test the user to update authuser profile successfully'
        payload = {'name':'matthew1','email':'matthew@gmail.com','password':'YouCrazyWIthProgrammingokaywithjavascript'}
        
        resp = self.client.put(GET_USER_PROFILE(self.user.id),payload)

        self.assertEqual(resp.status_code,status.HTTP_200_OK)
        # print(resp.data)
        IsuserExits = get_user_model().objects.filter(email=resp.data['email']).exists()
        user = get_user_model().objects.get(email=resp.data['email'])
        
        self.assertTrue(user.check_password(payload.get('password')))
        self.assertTrue(IsuserExits)

    def test_unauth_user_update_profile(self):
        'test if unauth user can upate thier proifile'
        payload = {'name':'matthew1','email':'matthew@gmail.com','password':'YouCrazyWIthProgrammingokaywithjavascript'}
        user = create_user(**payload)

        resp = self.client.patch(GET_USER_PROFILE(self.user.id),payload)
        

        self.assertEqual(resp.status_code,status.HTTP_400_BAD_REQUEST)