from django.contrib.auth import authenticate   # type: ignore
from rest_framework.views import APIView        # type: ignore
from rest_framework.response import Response        # type: ignore
from rest_framework import status                   # type: ignore
from rest_framework_simplejwt.tokens import RefreshToken        # type: ignore
from rest_framework.permissions import IsAuthenticated        # type: ignore
from rest_framework_simplejwt.authentication import JWTAuthentication      # type: ignore
from UserServices.models import Users        # type: ignore   


class SignupView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        profile_pic = request.data.get('profile_pic')

        if username is None or password is None or email is None:
            return Response(data='Please provide username, password, and email', status=status.HTTP_400_BAD_REQUEST)

        user = Users.objects.create_user(username=username, password=password, email=email, profile_pic=profile_pic)
        user.save()

        refresh = RefreshToken.for_user(user)
        access =refresh.access_token
        access['username'] = user.username
        access['email'] = user.email
        access['profile_pic'] = user.profile_pic

        return Response({'access':str(access),'refresh':str(refresh),'message':'User Created Successfully'},status=status.HTTP_201_CREATED)

class LoginView(APIView):
     def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response(data='Please provide both username and password')
        user = authenticate(request, username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            access =refresh.access_token
            access['username'] = user.username
            access['email'] = user.email
            access['profile_pic'] = user.profile_pic

            return Response({
                'refresh': str(refresh),
                'access': str(access),
            })
        else:
            return Response(data='Invalid credentials',status=status.HTTP_400_BAD_REQUEST)
        
def get(self,request):
            return Response(data='Please Use Post Method to Login',status=status.HTTP_400_BAD_REQUEST)
  
class PublicAPIView(APIView):
    def get(self, request):
        return Response(data='This is a publicly accessible API',status=status.HTTP_400_BAD_REQUEST)

class ProtectedAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data='This is a protected API. You can access this because you are authenticated.',status=status.HTTP_400_BAD_REQUEST)
