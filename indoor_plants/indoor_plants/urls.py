from django.contrib import admin
from django.urls import path, include, re_path
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
    # Swagger UI for API documentation
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Admin site
    path('admin/', admin.site.urls),

    # Authentication app URLs
    path('accounts/', include('authentication.urls')),  # Changed auth/ to accounts/

    # Add more app URLs here as you go
]