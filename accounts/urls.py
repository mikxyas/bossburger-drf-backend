from django.urls import path, include
# from .api import RegisterAPI, LoginAPI, UserAPI, UserAdminAPI
from rest_framework import routers
from .api import RegisterViewSet

router = routers.DefaultRouter()
router.register('api/auth/register', RegisterViewSet, 'register')

urlpatterns = [
    path('api/auth/', include('rest_auth.urls')),
    path('api/auth/user/', include('allauth.urls'), name='get user'),
]

urlpatterns += router.urls
