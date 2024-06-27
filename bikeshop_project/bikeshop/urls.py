from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BikeViewSet, CustomerViewSet, SaleViewSet

router = DefaultRouter()
router.register(r'bikes', BikeViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'sales', SaleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
