from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model



class CreateUserSerializer(ModelSerializer):


    class Meta:
        model = get_user_model()
        fields = ('name','password','email',)
        