from rest_framework import serializers
from .models import Prospecto

class ProspectoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Prospecto
        fields = '__all__'