from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, StockViewSet

router=DefaultRouter()
router.register(r"Product", ProductViewSet, basename='products')
router.register(r"Stock", StockViewSet, basename='stocks')
urlpatterns=[path("",include(router.urls))]