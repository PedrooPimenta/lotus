from rest_framework import serializers
from perfil.models import Perfil,UserHasPerfil
from product.models import Product,Suits,Pants, WomenSuit,Accessories,UserHasSuits,Sales,DataDash
from django.contrib.auth.models import User as DjangoUser 

class DjangoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoUser
        fields = ['username', 'email', 'first_name', 'last_name', 'username', 'password']

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class UserHasPerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHasPerfil
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SuitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suits
        fields = '__all__'

class PantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pants
        fields = '__all__'

class WomenSuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = WomenSuit
        fields = '__all__'

class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = '__all__'

class UserHasSuitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHasSuits
        fields = '__all__'

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

class DataDashSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataDash
        fields = '__all__'
