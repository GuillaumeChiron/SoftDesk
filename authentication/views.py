from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from authentication.permissions import IsUser
from authentication.serializers import UserSerializer
from authentication.models import User


class UserViewset(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all().order_by("id")
        return queryset

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated(), IsUser()]
