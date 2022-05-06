from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from zebrands.products.models import Product


class PostProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    sku = serializers.CharField(required=True, validators=[UniqueValidator(queryset=Product.objects.all())])

    class Meta:
        model = Product
        fields = '__all__'


class GetProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1
