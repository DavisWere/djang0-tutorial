from datetime import timedelta
from django.utils.timezone import make_aware
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from core.models import *


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

        def to_representation(self, instance):
            data = super().to_representation(instance)
            data.pop('password')
            return data


class SalarySerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=User.objects.all(), required=False)

    class Meta:
        model = Salary
        fields = ['id', 'employee', 'base_salary', 'overtime',
                  'bonuses', 'deductions', 'net_salary']

    def validate(self, data):
        overtime = data.get('overtime', 0)
        if 'overtime' == 0:
            data['bonuses'] = 0
        elif 'overtime' <= str(8):  # think of if overtime is > 1 but 8
            data['bonuses'] = 5000
        else:
            data['bonuses'] = 10000
        return super().validate(data)

    def create(self, validated_data):
        employee = validated_data.pop('employee', None)
        employee = Salary.objects.create(**validated_data)

        return employee

    def update(self, instance, validated_data):
        employee = validated_data.pop('employee', None)
        employee = super().update(instance, validated_data)
        employee.save()
        if employee is not None:
            instance.employee = employee
        instance.save()

        return instance
