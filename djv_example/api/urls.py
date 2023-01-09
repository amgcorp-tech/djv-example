from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register("users", MyViewSet, basename="users_example")


urlpatterns = [] + router.urls
