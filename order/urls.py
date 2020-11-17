from django.urls import path, include
from rest_framework import routers
from .api import OrderViewSet, AdminOrderViewSet, AdminAllOrderViewSet
from knox import views as knox_views

router = routers.DefaultRouter()
router.register('api/order', OrderViewSet, 'orders')
router.register('api/admin/order', AdminOrderViewSet, 'admin order')
router.register('api/admin/order/all', AdminAllOrderViewSet, 'all admin order')
urlpatterns = router.urls
