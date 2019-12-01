from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('payment/<int:product_pk>/<int:art_pk>/', views.payment, name='payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    path('product/<int:design_pk>/', views.ProductDetailView.as_view(), name='productDetail_page'),
    path('edit/product/<int:art_pk>/', views.ProductDesignEditView.as_view(), name='editProduct_page'),
]
