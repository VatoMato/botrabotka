# bot/models/order.py   Иправленно по Промту 14
from tortoise.models import Model
from tortoise import fields

class Order(Model):
    id = fields.UUIDField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="orders")  # Используем строковый путь
    service_type = fields.CharField(max_length=100)
    status = fields.CharField(max_length=20, default="created")
    created_at = fields.DatetimeField(auto_now_add=True)
    closed_at = fields.DatetimeField(null=True)
    amount = fields.DecimalField(max_digits=10, decimal_places=2)
    media_id = fields.CharField(max_length=100)   # Иправленно по Промту 16

    class Meta:  # type: ignore  # Исправлено по Промту 14
        table = "orders"