from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from rest_framework_simplejwt.views import TokenRefreshView

from . import views
from .views import MyTokenObtainPairView, RegisterUserAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="DRF Notes API",
        default_version="v1",
        description="DRF Notes API with JWT authentication",
        contact=openapi.Contact(url="https://www.linkedin.com/in/daniel-pyrzanowski-77503b251"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = routers.SimpleRouter()
router.register(r"notes", views.NoteViewSet, basename="note")

urlpatterns = [
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("users/me/", views.getMe),
    path("users/new/", RegisterUserAPIView.as_view()),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + router.urls
