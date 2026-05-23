from rest_framework import serializers
from .models import SubscriptionType, Subscription
from django.contrib.auth.models import User

class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Subscription
        fields = '__all__'
