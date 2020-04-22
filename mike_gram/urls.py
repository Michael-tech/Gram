from django.urls import path, include

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token


admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("", TemplateView.as_view(template_name="pages/about.html"), name="about"),

    path("users/", include("users.urls", namespace="users")),
    path("gram/", include("gram.urls", namespace="gram")),

    # Allauth
    path("accounts/", include("allauth.urls")),
    # Auth-Token resf
    path("auth-token/", obtain_auth_token),

   #API
    path('api/v1.0/', include('gram.api.urls')),

    
]
