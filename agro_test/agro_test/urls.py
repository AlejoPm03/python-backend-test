# Django
from django.contrib import admin
from django.conf import settings
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.urls import path, include, re_path
# Rest framework
from rest_framework import permissions
# Swagger
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# Swagger schema view
schema_view = get_schema_view(
	openapi.Info(
		title = "Test agro API",
		default_version = "v1",
		description = "Simple test of agro control"
	),
	public = True,
	permission_classes = [ permissions.AllowAny ],
)


# Redirects root to swagger
def root_redirect(request):
	return redirect("/swagger", permanent = True)


# Django patterns
required_urlpatterns = [
	# Django admin
	path("admin/", admin.site.urls),
	# Browsable API
	path("api-auth/", include("rest_framework.urls")),
]

# Swagger patterns
api_documentation_urlpatterns = [
	# Swagger
	re_path(r"swagger(?P<format>.json|.yaml)", schema_view.without_ui(cache_timeout = 0), name = "schema-json"),
	path(r"swagger", schema_view.with_ui("swagger", cache_timeout = 0), name = "schema-swagger-ui")
]

urlpatterns = [
	# Root
	path("", root_redirect),
	# Apps
	path("", include("apps.producer.urls")),
	path("user/", include("apps.user.urls")),
] + required_urlpatterns + api_documentation_urlpatterns

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)