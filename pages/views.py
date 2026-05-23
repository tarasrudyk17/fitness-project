from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from subscriptions.models import Subscription
from subscriptions.models import SubscriptionType

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def rules(request):
    return render(request, 'pages/rules.html')

def contacts(request):
    return render(request, 'pages/contacts.html')

def subscriptions(request):
    return render(request, 'pages/subscriptions.html')

@login_required
def profile(request):
    user = request.user
    active_subscription = Subscription.objects.filter(user=user, is_active=True).first()
    return render(request, 'pages/profile.html', {
        'active_subscription': active_subscription
    })

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'pages/register.html', {'form': form})

def subscriptions(request):
    subscription_types = SubscriptionType.objects.all()
    return render(request, 'pages/subscriptions.html', {'subscription_types': subscription_types})
