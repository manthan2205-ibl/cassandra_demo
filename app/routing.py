from django.urls import path

from . import consumers

websocket_urlpatterns = [
  path('ws/<str:group_id>/<str:admin_id>/', consumers.MessageConsumer.as_asgi()),

  
]