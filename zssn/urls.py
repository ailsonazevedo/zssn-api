from django import views
from django.contrib import admin
from django.db import router
from django.urls import include, path, re_path
from rest_framework import routers, permissions
from survivor.views import InventoryViewSet, SurvivorViewSet, ItemViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.SimpleRouter()
router.register(r'survivors', SurvivorViewSet)
router.register(r'items', ItemViewSet)
router.register(r'inventories', InventoryViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="ZSSN API",
      default_version='v1',
      description="Api para rede social pós apocalipse zumbi.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += router.urls