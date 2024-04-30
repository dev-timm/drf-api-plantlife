from django.urls import path
from advertisements import views

urlpatterns = [
    path('advertisements/', views.AdvertisementList.as_view()),
    path('advertisements/<int:pk>/', views.AdvertisementDetail.as_view())
]
