from django.urls import path, include

from .views import register


urlpatterns = [
    path('register', register.RegisterCustomerAPIView.as_view(), name='register')
]