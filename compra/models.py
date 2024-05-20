from django.db import models
from django.contrib.auth.models import User

# Create your models here.request

class Transaccion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buy_order = models.CharField(max_length=50)
    session_id = models.CharField(max_length=50)
    amount = models.IntegerField()
    status = models.CharField(max_length=20)
    card_number = models.CharField(max_length=4)
    accounting_date = models.CharField(max_length=10)
    transaction_date = models.CharField(max_length=50)
    authorization_code = models.CharField(max_length=10)
    payment_type_code = models.CharField(max_length=10)
    response_code = models.IntegerField()
    installments_number = models.IntegerField()

    def __str__(self):
        return f'Transaccion {self.buy_order} - {self.status}'