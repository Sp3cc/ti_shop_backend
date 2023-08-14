from django.shortcuts import render

from products.serializer import ProductSerializer

from .models import Product
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView

class ProductView(ListCreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        # self.permission_classes = [IsAdminUser]
        return super().post(request, *args, **kwargs)
