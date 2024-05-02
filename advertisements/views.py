from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api_plantlife.permissions import IsOwnerOrReadOnly
from .models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementList(generics.ListCreateAPIView):
    """
    A view to list and create advertisements
    """

    serializer_class = AdvertisementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Advertisement.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'owner__profile'
    ]
    search_fields = [
        'owner__username',
        'title',
        'plant_type'
    ]
    ordering_fields = [
        'created_on',
        'price'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdvertisementDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A view to retrieve, update and delete advertisements
    """

    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Advertisement.objects.all()
