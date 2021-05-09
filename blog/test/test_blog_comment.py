from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model



class TestComment(TestCase):
    'now this comment test test both auth user and unauth user because both should be able to comment on a post'
    pass