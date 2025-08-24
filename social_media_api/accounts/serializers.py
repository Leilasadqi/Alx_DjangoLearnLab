from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token


from .models import User




class UserSerializer(serializers.ModelSerializer):
followers_count = serializers.IntegerField(source='followers.count', read_only=True)
following_count = serializers.IntegerField(source='following.count', read_only=True)


class Meta:
model = User
fields = [
'id', 'username', 'email', 'first_name', 'last_name',
'bio', 'profile_picture', 'followers_count', 'following_count'
]
read_only_fields = ['id', 'followers_count', 'following_count']




class RegisterSerializer(serializers.ModelSerializer):
password = serializers.CharField(write_only=True)


class Meta:
model = User
fields = ['username', 'email', 'password']


def validate_password(self, value):
validate_password(value)
return value


def create(self, validated_data):
user = User.objects.create_user(
username=validated_data['username'],
email=validated_data.get('email', ''),
password=validated_data['password'],
)
Token.objects.get_or_create(user=user)
return user




class LoginSerializer(serializers.Serializer):
username = serializers.CharField()
password = serializers.CharField(write_only=True)


def validate(self, attrs):
user = authenticate(username=attrs['username'], password=attrs['password'])
if not user:
raise serializers.ValidationError('Invalid credentials')
attrs['user'] = user
return attrs
