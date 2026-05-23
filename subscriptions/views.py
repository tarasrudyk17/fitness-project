from rest_framework import viewsets
from .models import SubscriptionType, Subscription
from .serializers import SubscriptionTypeSerializer, SubscriptionSerializer
from django.shortcuts import render

class SubscriptionTypeViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionType.objects.all()
    serializer_class = SubscriptionTypeSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

def subscription_types_view(request):
    subscription_types = SubscriptionType.objects.all()
    return render(request, 'subscriptions/subscriptions.html', {
        'subscription_types': subscription_types
    })