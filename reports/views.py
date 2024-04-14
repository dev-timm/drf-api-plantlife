from rest_framework import generics, permissions
from drf_api_plantlife.permissions import IsOwnerOrReadOnly
from .models import Report
from .serializers import ReportSerializer


class ReportList(generics.ListCreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Report.objects.all()

    # disable default pagination
    # https://stackoverflow.com/questions/52474430/disable-pagination-when-not-requesting-any-page-in-djangorestframework
    def paginate_queryset(self, queryset):
        if self.paginator and self.request.query_params.get(self.paginator.page_query_param, None) is None:
            return None
        return super().paginate_queryset(queryset)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReportDetail(generics.RetrieveDestroyAPIView):
    serializer_class = ReportSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Report.objects.all()

