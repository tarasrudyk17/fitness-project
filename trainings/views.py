from rest_framework import viewsets
from .models import Training
from .serializers import TrainingSerializer
from .serializers import TrainingRegistrationSerializer
from .models import TrainingRegistration
from users.permissions import IsAdmin
from subscriptions.models import SubscriptionType
from subscriptions.serializers import SubscriptionTypeSerializer
from rest_framework import permissions

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

class TrainingRegistrationViewSet(viewsets.ModelViewSet):
    queryset = TrainingRegistration.objects.all()
    serializer_class = TrainingRegistrationSerializer


class TrainingRegistrationViewSet(viewsets.ModelViewSet):
    queryset = TrainingRegistration.objects.all()
    serializer_class = TrainingRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Автоматично підставити користувача, що виконує запит
        serializer.save(user=self.request.user)
