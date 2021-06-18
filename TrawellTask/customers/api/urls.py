from django.urls import path
from . import views


urlpatterns = [
    path('customers/', views.CustomerListCreateAPIView.as_view(), name='customer_list'),
    path('passports/', views.PassportListCreateAPIView.as_view(), name='passport_list'),
    path('passport/<int:pk>', views.PassportDetailAPIView.as_view(), name='passport_actions'),
    path('customer/<int:pk>', views.CustomerDetailAPIView.as_view(), name='customer_actions'),
]
