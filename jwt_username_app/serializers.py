from rest_framework import serializers
from jwt_username_app.models import emp

class empSerializer(serializers.ModelSerializer):
     class Meta:
        model = emp
        fields = '__all__'