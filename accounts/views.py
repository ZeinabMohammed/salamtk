from django.shortcuts import render
from .models import UserProfile
from rest_framework import permissions,viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import filters
from .serializers import UserProfileSerializer,UserCreateSerializer
from . import paginations
# from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from rest_framework.views import APIView 
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from django.http import HttpResponse,JsonResponse, Http404
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import permissions, status
class GithubLogin(SocialLoginView):
	adapter_class = GitHubOAuth2Adapter
	# callback_url  = CALLBACK_URL_YOU_SET_ON_GITHUB
	client_class  = OAuth2Client
# API views
class FacebookLogin(SocialLoginView):
	adapter_class = FacebookOAuth2Adapter

#Registerview
class UserCreate(CreateAPIView):
	"""create the user"""
	# queryset 		   = UserProfile.objects.all()
	serializer_class   = UserCreateSerializer
	# permission_classes = (permissions.AllowAny,)
	def post(self,request, format=None):
		# permission_classes = [IsOwnerOrReadOnly,]
		serializer 		   = UserCreateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.user=self.request.user
			serializer.save(request)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProfileListAPI(APIView):
	"""list all profiless or create new one"""

	def get(self, request, format=None):
		permission_classes = [AllowAny,]
		profiles  		   = UserProfile.objects.all()
		serializer 		   = UserProfileSerializer(profiles, many=True,context={'request': request})
		return Response(serializer.data)

	def post(self,request, format=None):
		permission_classes = [IsOwnerOrReadOnly,]
		serializer 		   = UserProfileSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetailAPI(APIView):
	"""RUD"""
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	def get_object(self,pk):
		try:
			return UserProfile.objects.get(pk=pk)
		except UserProfile.DoesNotExist:
			raise Http404
	def get(self, request,pk, format=None):
		profile = self.get_object(pk)
		serializer = UserProfileSerializer(profile,context={'request': request})
		return Response(serializer.data)
	def put(self, request,pk, format=None):
		profile = self.get_object(pk)
		serializer = AdSerializer(profile, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
	def delete(self, request, pk, format=None):
		profile = self.get_object(pk)
		profile.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class UserProFileList(viewsets.ModelViewSet):
	# permission_classes  = (permissions.IsAuthenticatedOrReadOnly,)
	queryset 			= UserProfile.objects.all()
	serializer_class	= UserProfileSerializer
	pagination_class  	= paginations.ProfilePagination
	filter_backends 	= [DjangoFilterBackend, SearchFilter,]
	filterset_fields    = ['__all__']
	search_fields 	    = ['user','address','checkup_price','city','country',]
	ordering            = ['user',]


