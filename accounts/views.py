from django.shortcuts import render
from .models import UserProfile
from rest_framework import permissions,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from .serializers import UserProfileSerializer
from . import paginations
# from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView

class GithubLogin(SocialLoginView):
	adapter_class = GitHubOAuth2Adapter
	# callback_url  = CALLBACK_URL_YOU_SET_ON_GITHUB
	client_class  = OAuth2Client
# API views
class FacebookLogin(SocialLoginView):
	adapter_class = FacebookOAuth2Adapter

class UserProFileList(viewsets.ModelViewSet):
	# permission_classes  = (permissions.IsAuthenticatedOrReadOnly,)
	queryset 			= UserProfile.objects.all()
	serializer_class	= UserProfileSerializer
	pagination_class  	= paginations.ProfilePagination
	filter_backends 	= [DjangoFilterBackend, SearchFilter,]
	filterset_fields    = ['__all__']
	search_fields 	    = ['user','address','checkup_price','city','country',]
	ordering            = ['user',]
