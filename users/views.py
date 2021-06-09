# from rest_framework.viewsets import ModelViewSet,ViewSetMixin
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework import mixins, serializers, status
from rest_framework.authtoken.views import ObtainAuthToken
from . import serializer
from rest_framework.renderers import api_settings
from rest_framework import permissions,authentication
from . import permissions as mypermissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
import random,string,smtplib



class CreateUser(GenericViewSet,mixins.CreateModelMixin):
    serializer_class = serializer.CreateUserSerializer




class LoginUser(ObtainAuthToken):
    serializer_class =serializer.LoginSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class ProfileViewSet(ModelViewSet):
    'this view can update and get a list of all the user to update u should use patch--for your javascript'
    serializer_class = serializer.UserProfileSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (permissions.IsAuthenticated,mypermissions.IsOWner,)
    authentication_classes = (authentication.TokenAuthentication,)


    def get_serializer_class(self):
        if self.action == 'upload_imageAction':
            return serializer.UserProfileImageSerializer
        
        return self.serializer_class

    def list(self, request):
        'this return the autheticated user'
        user = get_user_model().objects.get(id=request.user.id)

        serializer = self.serializer_class(user,many=False)

        return Response(serializer.data)



    @action(detail=True,methods=['post',],url_path='upload_image')
    def upload_imageAction(self, request, pk=None):
        user = self.get_object()
        # print(request.data)
        imageserialzer = serializer.UserProfileImageSerializer(user,data=request.data)
        if imageserialzer.is_valid():
            imageserialzer.save()

        return Response(imageserialzer.data)




class ForgotPasswordApiView(APIView):
    serializer_class = serializer.ForgotPasswordSerializer

    def _random_password(self):
        'this is a private function that returns 7 character string'
        randomStringOfCharacters = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 9))
        return randomStringOfCharacters

    def post(self, request, format=None):
        """
        this will get the user email which is unquie and reset his password then send that
        reset password to the email so they can login and change thier password in the profile
        """
        Serialized_data = self.serializer_class(data=request.data)
        if Serialized_data.is_valid():
            email = Serialized_data.data.get('email')
            if get_user_model().objects.filter(email=email).exists():
                "if the email exits in the data base get that user and change his password"
                user = get_user_model().objects.get(email=email)
                newpassword = self._random_password()
                try:
                    # afer we send the mail and it went successully then we can change the password
                    send_mail(
                        f'Hey {user.name}  Your Password',
                        """ 
                            Follow This Steps To Stay Secured\n\n
                            This is Your New Password '{newpassword}',
                            now login with your new password 
                            After you login go to your profile Scroll Down 
                            And CareFully Change The Password to Your Password To What You Like!!!
        
                        """,
                        settings.EMAIL_HOST_USER #From:this will be the site Email,
                        [user.email] ,#To: this will be the user that has forgoten his password,
                        fail_silently=False,    
                    )
                    user.set_password(newpassword)
                    user.save()
                except smtplib.SMTPException:
                    return Response(data={"error":'Network Error please Try again'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                return Response(data={"success":'Succefully Reset Password'},status=status.HTTP_200_OK)
            else:
                return Response(data={"error":"No User With This email"})

                

        else:
            return Response(data={"error":"Please enter a valid Email"})
