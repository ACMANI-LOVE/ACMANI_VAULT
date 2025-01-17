
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from app.views import *

# Initialize
router = DefaultRouter()
router.register(r'configs', ConfigsViewSet)
router.register(r'groups', GroupsViewSet)
router.register(r'tasks', TasksViewSet)
router.register(r'posts', PostsViewSet)
router.register(r'prompts', PromptsViewSet)
router.register(r'requests', RequestsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('', include(router.urls)),
]
