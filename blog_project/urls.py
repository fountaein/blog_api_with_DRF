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
from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from blog_api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("blog_api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/rest-auth/", include("rest_auth.urls")),
    path("api/v1/rest-auth/registration/", include("rest_auth.registration.urls")),
    path("api/v1/account/", include("allauth.urls")),
    url(
        r"^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$",
        confirm_email,
        name="account_confirm_email",
    ),
    url(
        r"^registration/complete/$", views.success_view, name="account_confirm_complete"
    ),
    url(
        r"^registration/account-email-verification-sent/",
        views.redirection_view,
        name="account_email_verification_sent",
    ),
    url(
        r"^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$",
        views.redirection_view,
        name="password_reset_confirm",
    ),

]
