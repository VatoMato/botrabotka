# bot\models\dispute.py
from tortoise.models import Model
from tortoise import fields

class Dispute(Model):
    id = fields.UUIDField(pk=True)
    order = fields.ForeignKeyField('models.Order')
    user = fields.ForeignKeyField('models.User')
    description = fields.TextField()
    status = fields.CharField(max_length=20, default='open')
    media_url = fields.CharField(max_length=255, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    resolved_at = fields.DatetimeField(null=True)

    class Meta:  # type: ignore  # Исправлено по Промту 14
        table = "disputes"