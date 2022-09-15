from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<int:pk>', client_view),
    path('message_list/', message_list)
]
