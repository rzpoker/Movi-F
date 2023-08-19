from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.MovieViewset)
urlpatterns = [

    path('viewsets/', include(router.urls)),
    ]