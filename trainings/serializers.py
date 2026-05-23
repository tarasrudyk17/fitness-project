from rest_framework import serializers
from .models import Training
from django.contrib.auth.models import User
from .models import TrainingRegistration

class TrainingSerializer(serializers.ModelSerializer):
    trainer = serializers.StringRelatedField()

    class Meta:
        model = Training
        fields = '__all__'

class TrainingRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingRegistration
        fields = ['id', 'user', 'training', 'registered_at']
        read_only_fields = ['registered_at']
