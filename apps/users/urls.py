from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, sign_in

router = routers.DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("login", sign_in)
]