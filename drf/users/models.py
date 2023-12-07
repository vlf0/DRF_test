from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUser(AbstractUser):
    last_login = models.DateTimeField(_("last login"), default=timezone.now)
    pass

