from django.urls import path
from .views import get_exchange_rate

urlpatterns = [
    path('get_exchange_rate/', get_exchange_rate, name='get_exchange_rate'),
    path('get_currency_names/', get_currency_names, name='get_currency_names'),
    path('', TemplateView.as_view(template_name='index.html'), name='index')
]
