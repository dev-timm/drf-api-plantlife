from rest_framework import generics, permissions
from drf_api_plantlife.permissions import IsOwnerOrReadOnly
from .models import Bookmark
from .serializers import BookmarkSerializer


class BookmarkList(generics.ListCreateAPIView):
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Bookmark.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookmarkDetail(generics.RetrieveDestroyAPIView):
    serializer_class = BookmarkSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Bookmark.objects.all()
