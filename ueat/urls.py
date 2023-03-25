from django.urls import path

from ueat import views


urlpatterns = [
    path('', views.home, name='home'),
    path('show/<str:pk>', views.show, name='show'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    path('customer_service', views.customer_service, name='customer_service'),
    path('store_locator', views.store_locator, name='store_locator'),
    path('led-bulb/<str:slug>', views.led_bulb, name='led-bulb'),
    path('sunlight-fans/<str:slug>', views.sunlight_fans, name='sunlight-fans'),
    path('sunlight_inverter/<str:slug>', views.sunlight_inverter, name='sunlight_inverter'),
    path('sunlight_cooler/<str:slug>', views.sunlight_cooler, name='sunlight_cooler'),
    path('query-form', views.query_form, name='query-form'),
    path('products', views.products, name='products'),

]

