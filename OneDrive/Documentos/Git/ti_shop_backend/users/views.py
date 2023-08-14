from django.shortcuts import render

from users.serializer import UserSerializer
from .models import User
from rest_framework.generics import ListCreateAPIView

class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
