from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
import uuid
from django.urls import reverse
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password





# MY CUSTOMUSER
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    user_login = models.CharField(max_length=180,null=True,blank=True)
    user_nicename= models.CharField(max_length=180,null=True,blank=True)
    email = models.EmailField(_('emailaddress'), unique=True)
    # email = models.EmailField(
    #     verbose_name='email address',
    #     max_length=255,
    #     unique=True,
    # )
    # email = models.EmailField(unique=True ,verbose_name='email address', )
    user_url= models.CharField(max_length=180,null=True,blank=True)
    user_registered = models.DateTimeField(_("date_joined"),default=date.today)
    user_activationKey=models.CharField(max_length=180,null=True,blank=True)
    user_status=models.IntegerField(blank=True, null=True)
    displayname=models.CharField(max_length=180,null=True,blank=True)

    change_pw = models.BooleanField(default=True)
    is_staff = models.BooleanField(_("is_staff"), default=False)
    is_active = models.BooleanField(_("is_active"), default=True)
    # isCustomer = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # objects = CustomUserManager()
    objects = CustomUserManager()

    class Meta:
        ordering = ("id",)
        verbose_name = _("Accounts")
        verbose_name_plural = _("Acconts")

    def get_short_name(self):
       
        if self.displayname != "":
            return self.displayname
        else:
            return str(self.email)




