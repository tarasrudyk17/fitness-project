from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrainingViewSet, TrainingRegistrationViewSet

router = DefaultRouter()
router.register(r'trainings', TrainingViewSet)
router.register(r'registrations', TrainingRegistrationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
