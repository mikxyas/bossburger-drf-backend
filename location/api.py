from .serializers import LocationSerializer
from rest_framework import viewsets, generics,permissions
from .models import Location

class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = {
        permissions.IsAuthenticated
    }
    serializer_class = LocationSerializer
    
    def get_queryset(self):
        return self.request.user.locations.all()

    def perform_create(self, serializer):
        serializer.save(locCreator=self.request.user)
