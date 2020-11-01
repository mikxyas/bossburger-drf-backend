from django.urls import path, include
from rest_framework import routers
from .api import MenuItemViewSet
from knox import views as knox_views

router = routers.DefaultRouter()
router.register('api/menu', MenuItemViewSet, 'menu')

urlpatterns = router.urls
