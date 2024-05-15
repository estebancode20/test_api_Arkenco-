from django.urls import path, include
from rest_framework import routers
from crud import views

router = routers.DefaultRouter()
router.register(r'prospectos', views.ProspectoViewSet)

urlpatterns = [
    path('',include(router.urls))
]