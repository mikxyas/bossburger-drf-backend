from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.db import models
import datetime

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email,phone_number,name,password=None):
        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            name=name,
        )
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, password=None,phone_number=None, name=None, is_staff=True, is_admin=True,is_superuser=True):
        user = self.create_user(
            email=email,
            password=password,
            name=name,
            phone_number=phone_number,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    created_at = models.DateField(default=datetime.date.today)
    phone_number = models.CharField(max_length=12, default='+251')
    primary_loc_id = models.IntegerField(default=0)
    prevOrdType = models.CharField(max_length=200, default='none')
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'phone_number','name']
    objects = UserManager()

    def __str__(self):              
        return self.email
    
    # def token(self):
    #     token = AuthToken.objects.create(self)
    #     print(token[1])
    #     # if(not token):
    #         # token = AuthToken.objects.get(user=self)
    #     return (token[1])

    # def get_token(self):
