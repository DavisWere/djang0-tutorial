from django.shortcuts import render
import calendar
from django.utils import timezone
import requests
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from django.http import JsonResponse
import random
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
import os
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.conf import settings
from rest_framework.response import Response
from django.views import View
from rest_framework_simplejwt.views import TokenObtainPairView
from core.serializers import *
from core.models import *


class CustomObtainTokenPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            user = User.objects.filter(id=user.id)
        else:
            user = User.objects.all()
        return user


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [permissions.IsAuthenticated]
