
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class UserRegistrationSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=UserProfile.ROLE_CHOICES)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role = validated_data.pop('role')
        email = validated_data.pop('email')
        user = User.objects.create_user(**validated_data, email=email)
        UserProfile.objects.create(user=user, role=role)
        return user
