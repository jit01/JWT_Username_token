from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser

from jwt_username_app.models import emp
from jwt_username_app.serializers import empSerializer


class userview(ListCreateAPIView):
    queryset = emp.objects.all()
    serializer_class = empSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
