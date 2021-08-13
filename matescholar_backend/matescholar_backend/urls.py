"""matescholar_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db.models.query import QuerySet
from django.urls import path
from django.urls.conf import include
from rest_framework import routers, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
"""
class GetTokenViewSet(viewsets.ViewSet):
    queryset = Token.objects.all()

    def list(self, request):
        serializer = AuthTokenSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        token = get_object_or_404(self.queryset, pk=pk)
        serializer = AuthTokenSerializer(token)
        return Response(serializer.data)

router = routers.DefaultRouter()
router.register(r'user-token', GetTokenViewSet, basename='tokens')"""

urlpatterns = [
    path('api/', include("api.urls")),
    path('admin/', admin.site.urls),
]
