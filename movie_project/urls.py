"""
URL configuration for movie_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
# from movie_app_api import views
from movie_project import settings
from django.contrib.sitemaps.views import sitemap
from movie_app.sitemaps import MovieSitemap
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView # new


# from rest_framework import routers


admin.site.index_title = "Админ панель Django"

sitemaps = {
    "movies": MovieSitemap,
}

# router = routers.SimpleRouter()
# router.register(r'', views.MovieViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("movie_app.urls", namespace="index")),
    path("video/", include("video_player.urls", namespace="video_player")),
    path("user/", include("user.urls", namespace="user")),
    # debug
    path("__debug__/", include("debug_toolbar.urls")),
    # social auth
    re_path(r"^oauth/", include("social_django.urls", namespace="social")),
    # sitemap
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap",),
    # авторизация по токенам JWT
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_refresh'),
    # авторизация по токенам
    path("api/v1/drf-auth", include("rest_framework.urls")),
    path("api/v1/auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
    # API версия 1
    path("api/v1/", include("movie_app_api.urls")),
    # schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    #router
    # path("api/v1/", include(router.urls)), # for router
    # path("api/v2/", include("movie_app_api_v2.urls")), # API версия 2
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
