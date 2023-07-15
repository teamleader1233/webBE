from django.urls import path, include

from .views import bill, product

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'^bills', bill.BillViewSet, basename='bill')
router.register(r'^products', product.ProductViewSet, basename='product')

urlpatterns = [
    
]
    
urlpatterns += router.urls