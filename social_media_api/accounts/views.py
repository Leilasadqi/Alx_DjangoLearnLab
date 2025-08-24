from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication


from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import User




class RegisterView(generics.CreateAPIView):
serializer_class = RegisterSerializer
permission_classes = [permissions.AllowAny]


def create(self, request, *args, **kwargs):
response = super().create(request, *args, **kwargs)
user = User.objects.get(username=response.data['username'])
token, _ = Token.objects.get_or_create(user=user)
return Response({
'user': UserSerializer(user, context={'request': request}).data,
'token': token.key,
}, status=status.HTTP_201_CREATED)




class LoginView(APIView):
permission_classes = [permissions.AllowAny]


def post(self, request):
serializer = LoginSerializer(data=request.data)
serializer.is_valid(raise_exception=True)
user = serializer.validated_data['user']
token, _ = Token.objects.get_or_create(user=user)
return Response({
'user': UserSerializer(user, context={'request': request}).data,
'token': token.key,
}, status=status.HTTP_200_OK)




class ProfileView(generics.RetrieveUpdateAPIView):
serializer_class = UserSerializer
authentication_classes = [TokenAuthentication]
permission_classes = [permissions.IsAuthenticated]


def get_object(self):
return self.request.user
