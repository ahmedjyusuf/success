from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_mail(instance, subject: str,html_template):
        # subject = "Welcome to Meta Tutoring"
        # html_template = "welcome_email.html"
        user = instance.first_name if instance.first_name else instance.username
        context = {'user': user} # Add any context variables you want to pass to the template
        recipient_list = [instance.email]#[user_email]

        html_message = render_to_string(html_template, context)

        email = EmailMultiAlternatives(
            subject=subject,
            body=strip_tags(html_message),
            from_email=settings.EMAIL_HOST_USER,
            to=recipient_list,
        )
        email.attach_alternative(html_message, "text/html")
        email.send()