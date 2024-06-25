import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view


class APISchemeGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=True):
        schema = super().get_schema(request, public)

        if os.environ.get('DOMAIN'):
            schema.host = os.environ.get('DOMAIN')
            schema.base_path = '/api/v1'

        return schema


swagger_view = get_schema_view(
    openapi.Info(
        title='Affiliate API',
        default_version='v1',
        description='This is Backend API for Affiliate Application',
    ),
    public=True,
    generator_class=APISchemeGenerator,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', swagger_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('core.api.urls'), name='api'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
