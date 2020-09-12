

from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .permissions import IsAuthorOrReadOnly

from.models import Post, Category
from.serializers import PostSerializer , CategorySerializer





@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(
            instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
            reset_password_token.key),
        'site_name': "Blog App"
        
    }

    # render email text
    email_html_message = render_to_string('account/email/user_reset_password.html', context)
    email_plaintext_message = render_to_string('account/email/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Blog API"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@example.com",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()

@api_view()
def success_view(request):
    return Response("Email account has been activated")

class PostListView(generics.ListCreateAPIView):
    # permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    
    queryset=Post.objects.all()
    serializer_class= PostSerializer
  


class CategoryListView(generics.ListCreateAPIView):
    # permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    
    queryset=Category.objects.all()
    serializer_class= CategorySerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Post.objects.all()
    serializer_class= PostSerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Category.objects.all()
    serializer_class= CategorySerializer
