from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriptionTypeViewSet, SubscriptionViewSet
from subscriptions import views_site

router = DefaultRouter()
router.register(r'types', SubscriptionTypeViewSet)
router.register(r'', SubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('subscriptions/', views_site.subscription_types_view, name='subscriptions'),
    path('subscriptions/<int:sub_id>/purchase/', views_site.purchase_subscription, name='purchase_subscription'),
    path('payment-success/', views_site.payment_success, name='payment_success'),
]