"""
ASGI config for ChatPrj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack  # Для поддержки аутентификации в WebSocket
from ChatApp import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatPrj.settings')

# Получаем стандартное ASGI приложение для обработки HTTP запросов
django_asgi_app = get_asgi_application()

# Создаем конфигурацию для обработки HTTP и WebSocket запросов
application = ProtocolTypeRouter({
    "http": django_asgi_app,  # HTTP запросы обрабатываются стандартным приложением
    "websocket": AuthMiddlewareStack(  # Добавляем поддержку аутентификации для WebSocket
        URLRouter(
            routing.websocket_urlpatterns  # Маршруты WebSocket
        )
    ),
})
