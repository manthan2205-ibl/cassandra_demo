from django.urls import path

from . import consumers

websocket_urlpatterns = [
  path('ws/<str:group_id>/<str:user_id>/', consumers.MessageConsumer.as_asgi()),

  
]