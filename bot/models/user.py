# bot/models/user.py
from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    tg_id = fields.BigIntField(unique=True)
    full_name = fields.CharField(max_length=255)
    phone = fields.CharField(max_length=20, null=True)
    orders: fields.ReverseRelation["Order"]
    discount = fields.IntField(default=0)
    
    class Meta:
        table = "users"