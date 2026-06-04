from rest_framework.viewsets import ModelViewSet

from authentication.serializers import UserSerializer
from authentication.models import User


class UserViewset(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
