from rest_framework import serializers
from .models import UserProfile
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfile
from rest_auth.registration.serializers import RegisterSerializer
class UserProfileSerializer(serializers.ModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='accounts:profile-detail', source='UserProfile')
	class Meta:
		model  = UserProfile
		fields = ['id','user','title','description','address','url']

class UserCreateSerializer(RegisterSerializer):
	username         = serializers.CharField()
	email    		 = serializers.EmailField()
	phone_number     = serializers.CharField(min_length=11, write_only=True,
												validators=[UniqueValidator(queryset=
															UserProfile.objects.all())])
	class Meta:
		model  = UserProfile
		fields = ['id','username','email','phone_number','password','confirm_password']

	def create(self,validated_data):
		user = UserProfile.objects.create(
						username     = validated_data['username'],
						email 	     = validated_data['email'],
						phone_number = validated_data['phone_number'],
					)
		user.set_password(validated_data['password'])
		user.save()
		return user