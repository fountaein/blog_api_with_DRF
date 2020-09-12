"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from allauth.account.views import confirm_email,password_reset_from_key,password_reset_done
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from blog_api import views
from django.views.generic import TemplateView
from rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("blog_api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/rest-auth/", include("rest_auth.urls")),
    path("api/v1/rest-auth/registration/", include("rest_auth.registration.urls")),

    url(
        r"^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$",
        confirm_email,
        name="account_confirm_email",
    ),
    url(
        r"^registration/complete/$", views.success_view, name="account_confirm_complete"
    ),
 url(r'^api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
   
]







     
