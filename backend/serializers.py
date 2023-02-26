from rest_framework import serializers
from .models import *


class SliderSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Slider
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Product
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):    
    class Meta:
        model = FAQ
        fields = '__all__'