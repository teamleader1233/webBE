from django.urls import path, include

from .views import bill, product, blog

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('bills', bill.BillViewSet, basename='bill')
router.register('products', product.ProductViewSet, basename='product')
router.register('blogs', blog.BlogViewSet, basename='blog')

urlpatterns = [
    
]
    
urlpatterns += router.urls