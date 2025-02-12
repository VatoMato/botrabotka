# bot/models/user.py    Иззмененно по Промту 14
from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    tg_id = fields.BigIntField(unique=True)
    full_name = fields.CharField(max_length=255)
    phone = fields.CharField(max_length=20, null=True)
    # Order удален из импортов, связь через related_name
    discount = fields.IntField(default=0)
    
    class Meta:  # type: ignore  # Исправлено по Промту 14
        table = "users"