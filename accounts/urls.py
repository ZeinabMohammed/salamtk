
from django.urls import path, include
from rest_framework import routers


from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenVerifyView,
    TokenRefreshView,
	)
from .views import GithubLogin, FacebookLogin,UserProFileList

router = routers.DefaultRouter()
router.register('profiles', UserProFileList)
urlpatterns = [
	#Myviews
	path('', include(router.urls)),
	 #AllAuth paths
    path('rest-auth/', include('rest_auth.urls')),
	path('rest-auth/register/', include('rest_auth.registration.urls')),
    #social login
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/github/', GithubLogin.as_view(), name='github_login'),
	#Jwt jsonwebtoken urls
	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ]