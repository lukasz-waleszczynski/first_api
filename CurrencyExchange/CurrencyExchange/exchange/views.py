from django.shortcuts import render
from django.http import JsonResponse
from .models import Currency

def get_exchange_rate(request):
    currency_name = request.GET.get('currency_name', '')
    try:
        currency = Currency.objects.get(name=currency_name)
        return JsonResponse({'rate': currency.rate})
    except Currency.DoesNotExist:
        return JsonResponse({'error': 'Cuddency not found.'})
    
def get_currency_names(request):
    currencies = Currency.objects.values('name')
    currency_names = [currency['name'] for currency in currencies]
    return JsonResponse({'currency_names': currency_names})
