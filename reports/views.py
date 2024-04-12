from rest_framework import generics, permissions
from drf_api_plantlife.permissions import IsOwnerOrReadOnly
from .models import Report
from .serializers import ReportSerializer


class ReportList(generics.ListCreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Report.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReportDetail(generics.RetrieveDestroyAPIView):
    serializer_class = ReportSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Report.objects.all()

