# botrabotka
├── bot/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── bot.py          # Инициализация бота и диспетчера
│   │   └── middleware/     # Кастомные middleware
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── commands.py     # Обработчики /start и основных команд
│   │   ├── payments.py     # Логика работы с ЮKassa
│   │   └── orders.py       # Логика заказов и услуг
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py         # Модель пользователя
│   │   └── order.py        # Модель заказа со статусами
│   ├── services/
│   │   ├── database.py     # Асинхронный доступ к PostgreSQL
│   │   ├── storage.py      # Работа с S3-совместимым хранилищем
│   │   └── sharding.py     # Логика шардирования
│   ├── tasks/
│   │   ├── __init__.py
│   │   └── order_tasks.py  # Celery задачи для заказов
│   ├── utils/
│   │   ├── logging.py      # Настройка логов с интеграцией Loki
│   │   └── tracing.py      # Инструментация для Jaeger
│   └── config.py           # Конфигурация приложения
├── infrastructure/
│   ├── k8s/                # Kubernetes манифесты
│   ├── istio/              # Service Mesh конфигурация
│   └── chaos/              # Chaos Engineering тесты
├── deploy/
│   └── helm-charts/        # Helm чарты для деплоя
└── .env                    # Переменные окружения