# bot/models/order.py
from tortoise.models import Model
from tortoise import fields
from datetime import datetime

class Order(Model):
    id = fields.UUIDField(pk=True)
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="orders"
    )
    service_type = fields.CharField(max_length=100)
    status = fields.CharField(max_length=20, default="created")
    created_at = fields.DatetimeField(auto_now_add=True)
    closed_at = fields.DatetimeField(null=True)
    amount = fields.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        table = "orders"