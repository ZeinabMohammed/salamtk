
from django.urls import path, include
from rest_framework import routers


from rest_framework_simplejwt.views import(
                                    TokenObtainPairView,
                                    TokenVerifyView,
                                    TokenRefreshView,
                                    )
from .views import (GithubLogin, FacebookLogin,
                    UserProFileList, UserCreate,
                    ProfileListAPI, ProfileDetailAPI,
                    )
app_name='accounts'
router = routers.DefaultRouter()
# router.register('profiles', UserProFileList)
# router.register('register',UserCreate)
urlpatterns = [
    #Myviews
    path('register/',UserCreate.as_view(),name='register'),
    path('profiles',ProfileListAPI.as_view(),name='profiles-list'),
    path('profile/<pk>',ProfileDetailAPI.as_view(),name='profile-detail'),
    # path('', include(router.urls)),
    #PasswordLess
    # path('', include('drfpasswordless.urls')),
    #OAUTH
    # path('', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path('', include('rest_framework_social_oauth2.urls')),
    #AllAuth paths
    
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/register/', include('rest_auth.registration.urls')),
    #social login rest-auth
    # path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    # path('rest-auth/github/', GithubLogin.as_view(), name='github_login'),
    #Jwt jsonwebtoken urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ]