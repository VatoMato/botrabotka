# bot\models\payment.py
from tortoise.models import Model
from tortoise import fields

class Payment(Model):
    id = fields.UUIDField(pk=True)
    order = fields.ForeignKeyField('models.Order')
    amount = fields.DecimalField(max_digits=10, decimal_places=2)
    status = fields.CharField(max_length=20, default='pending')
    yookassa_id = fields.CharField(max_length=50)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "payments"