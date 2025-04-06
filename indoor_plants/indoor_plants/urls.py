from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Schema view for Swagger UI
schema_view = get_schema_view(
    openapi.Info(
        title="Indoor Plants Management API",
        default_version="v1",
        description="API for managing indoor plants, maintenance, and orders.",
        contact=openapi.Contact(email="support@example.com"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
   # Swagger UI (accessible at both root / and /swagger/)
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),

    # OpenAPI schema (JSON view)
    path('openapi/', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # Admin site
    path('admin/', admin.site.urls),

    # Authentication app URLs
    path('accounts/', include('authentication.urls')),

    # Plants app URLs
    path('plants/', include('plants.urls')),

    # Maintenance app URLs
    path('maintenance/', include('maintenance.urls')),  # Link maintenance app

    # Orders app URLs
    path('orders/', include('orders.urls')),  # Link orders app
]
