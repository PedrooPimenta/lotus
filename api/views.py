from django.shortcuts import render
from api.serializers import PerfilSerializer,UserHasPerfilSerializer,ProductSerializer,SuitsSerializer,PantsSerializer,WomenSuitSerializer,AccessoriesSerializer,UserHasSuitsSerializer,SalesSerializer,DataDashSerializer,DjangoUserSerializer
from perfil.models import Perfil,UserHasPerfil
from product.models import Product,Suits,Pants, WomenSuit,Accessories,UserHasSuits,Sales,DataDash
from django.contrib.auth.models import User as DjangoUser 
from rest_framework import viewsets, permissions

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = DjangoUser.objects.all()
    serializer_class = DjangoUserSerializer
    permission_classes = [
        permissions.AllowAny
    ]
class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    permission_classes = [
        permissions.AllowAny
    ]
class UserHasPerfilViewSet(viewsets.ModelViewSet):
    queryset = UserHasPerfil.objects.all()
    serializer_class = UserHasPerfilSerializer
    permission_classes = [
        permissions.AllowAny
    ]
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class SuitsViewSet(viewsets.ModelViewSet):
    queryset = Suits.objects.all()
    serializer_class = SuitsSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PantsViewSet(viewsets.ModelViewSet):
    queryset = Pants.objects.all()
    serializer_class = PantsSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WomenSuitViewSet(viewsets.ModelViewSet):
    queryset = WomenSuit.objects.all()
    serializer_class = WomenSuitSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class AccessoriesViewSet(viewsets.ModelViewSet):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class UserHasSuitsViewSet(viewsets.ModelViewSet):
    queryset = UserHasSuits.objects.all()
    serializer_class = UserHasSuitsSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class DataDashViewSet(viewsets.ModelViewSet):
    queryset = DataDash.objects.all()
    serializer_class = DataDashSerializer
    permission_classes = [
        permissions.AllowAny
    ]
