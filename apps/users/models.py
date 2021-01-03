from django.contrib.auth.models import AbstractUser
from django.db import models
from . import managers


class User(AbstractUser):
    username = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    referral_code = models.CharField(max_length=250, null=True, blank=True)
    USERNAME_FIELD = 'phone'
    objects = managers.UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.first_name} {self.phone}'

    def set_referral_code(self):
        self.referral_code = "{:06}".format(self.pk)

    def save(self, *args, **kwargs):
        if not self.referral_code:
            self.set_referral_code()
        super(User, self).save(*args, **kwargs)
