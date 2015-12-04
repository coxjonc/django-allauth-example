from django.contrib.auth.models import User
from django.db import models
from allauth.account.models import EmailAddress


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)

    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)
