from rest_framework import routers
from .api import LocationViewSet, AdminLocViewSet

router = routers.DefaultRouter()
router.register('api/locations', LocationViewSet, 'locations')
router.register('api/admin/locations', AdminLocViewSet, 'admin locations')

urlpatterns= router.urls