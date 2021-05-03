from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model



class CreateUserSerializer(ModelSerializer):


    def create(self,validate_data):
        email =validate_data.get('email')
        password =validate_data.get('password')
        name =validate_data.get('name')
        user = get_user_model().objects.create_user(email=email,name=name,password=password)

        return user

    class Meta:
        model = get_user_model()
        fields = ('name','password','email',)
        extra_kwargs = {
                        
                        'password':{'write_only':True,'min_length':5,'style':{'input_type':'password'}},
                        
                        }