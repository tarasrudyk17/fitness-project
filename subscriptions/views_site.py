from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import SubscriptionType, Subscription
from payments.models import Payment
from datetime import date, timedelta

@login_required
def purchase_subscription(request, sub_id):
    subscription_type = get_object_or_404(SubscriptionType, id=sub_id)
    
    if request.method == 'POST':
        method = request.POST.get('method')
        amount = subscription_type.price
        start = date.today()
        end = start + timedelta(days=subscription_type.duration_days)

        # Створюємо підписку
        subscription = Subscription.objects.create(
            user=request.user,
            subscription_type=subscription_type,
            start_date=start,
            end_date=end,
            is_active=True
        )

        # Створюємо оплату
        Payment.objects.create(
            user=request.user,
            subscription=subscription,
            amount=amount,
            method=method
        )

        return redirect('payment_success')

    return render(request, 'subscriptions/payment.html', {'subscription': subscription_type})

def payment_success(request):
    return render(request, 'subscriptions/success.html')

def subscription_types_view(request):
    subscription_types = SubscriptionType.objects.all()
    return render(request, 'subscriptions/subscriptions.html', {
        'subscription_types': subscription_types
    })