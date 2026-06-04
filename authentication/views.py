from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from authentication.serializers import UserSerializer
from authentication.models import User


class UserViewset(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
