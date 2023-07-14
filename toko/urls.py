from django.urls import path, include, URLPattern
from . import views

app_name = 'toko'

urlpatterns = [
     path('', views.HomeListView.as_view(), name='home-produk-list'),
     path('search/', views.search_feature, name='search-view'),
     path('skincare/', views.HomeListSkincare.as_view(), name='home-produk-skincare-list'),
     path('bathbody/', views.HomeListBathBody.as_view(), name='home-produk-bathbody-list'),
     path('others/', views.HomeListOthers.as_view(), name='home-produk-others-list'),
     path('product/<slug>/', views.ProductDetailView.as_view(), name='produk-detail'),
     path('checkout/', views.CheckoutView.as_view(), name='checkout'),
     path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
     path('remove_from_cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
     path('order-summary/', views.OrderSummaryView.as_view(), name='order-summary'),
     path('payment/<payment_method>', views.PaymentView.as_view(), name='payment'),
     path('paypal-return/', views.paypal_return, name='paypal-return'),
     path('paypal-cancel/', views.paypal_cancel, name='paypal-cancel'),
     path('contact/', views.contact, name='contact'),
     path('success/', views.success, name='success'),
     path('product/', views.product, name='product'),
     path('currencies/', include('currencies.urls')),
]
