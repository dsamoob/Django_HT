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


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


