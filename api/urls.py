from django.urls import path, include

from .views import bill

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'^bill', bill.BillViewSet, basename='bill')


urlpatterns = [
    
]
    
urlpatterns += router.urls