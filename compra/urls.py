from django.urls import path
from . import views

urlpatterns = [
  path('transaction/create/', views.transbank_create),
  path('transaction/reverse-or-cancel/<str:tokenws>', views.transbank_reverse_or_cancel),
  path('commit/<str:tokenws>', views.transbank_commit),
  path('get-status/<str:tokenws>/', views.transbank_get_status),
  path('transbank-capture/<str:tokenws>', views.transbank_capture)
]