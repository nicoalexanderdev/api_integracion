from rest_framework import serializers
from .models import Transaccion

class TransaccionSerializer(serializers.Serializer):
  class Meta:
    model = Transaccion
    fields = [
      'user', 
      'buy_order', 
      'session_id', 
      'amount', 
      'status', 
      'card_number', 
      'accounting_date', 
      'transaction_date', 
      'authorization_code',
      'payment_type_code',
      'response_code',
      'installments_number'
      ]
    
  def create(self, validated_data):
    return Transaccion.objects.create(**validated_data)