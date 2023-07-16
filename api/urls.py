from django.urls import path, include

from .views import bill, product

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('bills', bill.BillViewSet, basename='bill')
router.register('products', product.ProductViewSet, basename='product')

urlpatterns = [
    
]
    
urlpatterns += router.urls