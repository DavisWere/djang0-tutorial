from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from core.views import CustomObtainTokenPairView, UserViewSet, SalaryViewSet

core_router = DefaultRouter()
core_router.register(r'users', UserViewSet)
core_router.register(r'salary', SalaryViewSet)
url_patterns = core_router.urls

url_patterns += [
    path("token/request/", CustomObtainTokenPairView.as_view(), name="token_request"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),


]
