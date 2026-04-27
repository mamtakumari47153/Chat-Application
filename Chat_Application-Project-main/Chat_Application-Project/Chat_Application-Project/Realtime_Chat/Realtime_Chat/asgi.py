import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from Message_App.routing import websocket_urlpatterns  # ✅ adjust if app name is different

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Realtime_Chat.settings")
django.setup()

# For handling HTTP requests
django_asgi_app = get_asgi_application()

# Final ASGI application with WebSocket support
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
