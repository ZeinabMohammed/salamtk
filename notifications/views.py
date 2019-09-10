from django.shortcuts import render
from rest_framework import permissions,viewsets
from .serializers import NotificationSerializer
from .models import Notification
from . import utils

class NotificationView(viewsets.ModelViewSet):
	queryset         = Notification.objects.all()
	serializer_class = NotificationSerializer
	filterset_fields = '__all__'

