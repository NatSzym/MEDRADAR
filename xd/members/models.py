
# Create your models here.
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models
#
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, pesel, birth_date, gender, first_name='', last_name='', password=None, **extra_fields):
#         email = self.normalize_email(email)
#         user = self.model(email=email, pesel=pesel, birth_date=birth_date, gender=gender, first_name=first_name, last_name=last_name, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, pesel, birth_date, gender, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         return self.create_user(email, pesel, birth_date, gender, password, **extra_fields)
#
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField('User Email', unique=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     pesel = models.CharField(max_length=11, unique=True)
#     birth_date = models.DateField()
#     gender_choices = [('M', 'Male'), ('F', 'Female')]
#     gender = models.CharField(max_length=1, choices=gender_choices)
#
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['pesel', 'birth_date', 'gender']
#
#     def __str__(self):
#         return self.email

