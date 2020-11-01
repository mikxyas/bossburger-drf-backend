from django.urls import path, include
from rest_framework import routers
from .api import OrderViewSet
from knox import views as knox_views

router = routers.DefaultRouter()
router.register('api/order', OrderViewSet, 'orders')

urlpatterns = router.urls
