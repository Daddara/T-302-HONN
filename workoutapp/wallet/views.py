from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from wallet.models import Wallet


# Create your views here.
@login_required
def wallet(request):
    user_wallet = Wallet.objects.get(user=request.user)
    return render(request, 'wallet/wallet.html', context={'wallet': user_wallet})


