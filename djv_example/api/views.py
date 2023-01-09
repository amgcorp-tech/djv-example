from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from .serializers import *


class MyViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    A viewset for viewing user instances.
    """

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]
    queryset = get_user_model().objects.all()

    def get_serializer_class(self):
        return self.serializer_class

    def get_permissions(self):
        return [IsAuthenticated()]
