from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('slider', SliderView, basename='slider')
router.register('category', CategoryView, basename='category')
router.register('product', ProductView, basename='product')
router.register('FAQ', FAQView, basename='FAQ')

urlpatterns = [
    path('', include(router.urls)),
]