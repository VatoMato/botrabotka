highload-bot/
├── .env
├── requirements.txt
├── main.py
├── config.py
├── tortoise_config.py
├── handlers/
│   ├── __init__.py
│   ├── start.py
│   ├── services.py
│   ├── orders.py
│   ├── payment.py
│   ├── dispute.py
│   └── admin.py
├── keyboards/
│   ├── __init__.py
│   ├── main_menu.py
│   ├── inline.py
│   └── builders.py
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── order.py
│   ├── payment.py
│   └── dispute.py
├── services/
│   ├── __init__.py
│   ├── database.py
│   ├── yookassa.py
│   ├── scheduler.py
│   ├── minio_storage.py
│   ├── redis_cache.py
│   └── web_server.py
├── utils/
│   ├── __init__.py
│   ├── helpers.py
│   ├── validators.py
│   └── logger.py
├── migrations/
│   └── (автогенерируемые aerich файлы)
├── static/
│   ├── docs/
│   └── media/
├── tests/
│   ├── __init__.py
│   ├── test_handlers.py
│   └── test_services.py
├── docker-compose.yml
├── Dockerfile
└── README.md