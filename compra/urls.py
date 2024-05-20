from django.urls import path
from . import views

urlpatterns = [
  path('transaction/create/', views.transbank_create),
  path('transaction/reverse-or-cancel/<str:tokenws>', views.transbank_reverse_or_cancel),
  path('commit/<str:tokenws>', views.transbank_commit),
  path('get-status/<str:tokenws>/', views.transbank_get_status),
  path('transbank-capture/<str:tokenws>', views.transbank_capture),
  path('transaction-save/', views.transaction_save),
  path('get-dollar-value', views.get_dollar_value)
]