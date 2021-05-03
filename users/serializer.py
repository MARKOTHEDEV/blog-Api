from rest_framework import  serializers
from django.contrib.auth import get_user_model,authenticate



class CreateUserSerializer(serializers.ModelSerializer):


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


class UserProfileSerializer(serializers.ModelSerializer):



    class Meta:
        model = get_user_model()
        fields = ('name','password','email','name','image','bio')
        extra_kwargs = {
                        'password':{'read_only':True},
                        }



class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password =serializers.CharField(min_length=5)


    def validate(self,data):
        email =  data.get('email')
        password = data.get('password',None)

        
        user = authenticate(username=email,password=password)

        if user is  None:
            raise serializers.ValidationError(detail='User Does Not Exits Or Wrong Password')

        data['user'] = user
       
        return data