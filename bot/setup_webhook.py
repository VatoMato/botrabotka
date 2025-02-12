# setup_webhook.py     Добавлено из Промта 18
from yookassa import Webhook
from yookassa.domain.notification import WebhookNotificationEventType
from config import Config  # Импорт настроек

# Настройка вебхука для события "платеж успешен"
Webhook.add({
    "event": WebhookNotificationEventType.PAYMENT_SUCCEEDED,
    "url": f"{Config.WEBHOOK_URL}/yookassa-webhook"  # Ваш публичный URL
})

# Запустите скрипт в терминале: python setup_webhook.py