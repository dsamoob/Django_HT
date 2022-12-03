from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .filters import AdvertisementFilter
from .models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from .permissions import IsOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filterset_class = AdvertisementFilter


    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), ]
        if self.action in ["update", "partial_update", "destroy", ]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]

        return []

