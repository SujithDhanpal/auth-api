from django.shortcuts import render
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def home(request):
    return Response(data = "Hello! you are logged in now", status = status.HTTP_200_OK)
