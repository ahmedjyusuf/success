from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.conf import settings
from utils.email import send_mail


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_post_save(sender, created, instance, **kwargs):
    pass
    # if created and instance.email and 'metatutoring.us' not in instance.email.lower():
    #      send_mail(instance=instance,subject='Welcome to Meta Tutoring',
    #               html_template='welcome_email.html'
    #               )

@receiver(pre_save, sender=settings.AUTH_USER_MODEL)
def word_pre_save(sender, instance, **kwargs):
    pass

    