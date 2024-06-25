from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CarrierDataViewSet

router = DefaultRouter()
router.register(r'carriers', CarrierDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
