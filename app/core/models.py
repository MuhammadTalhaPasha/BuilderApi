import uuid
import os

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

from django.conf import settings


def userfile_file_path(instance, filename):
    """generate file_path for new userfile file"""
    ext = filename.split('.')[-1]
    # ADD CHANGEES HERE
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/user_files', filename)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError('User must have email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """create and a new save super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

#
# class Tag(models.Model):
#     """tag to be used for a user_file"""
#     name = models.CharField(max_length=255)
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE
#     )
#
#     def __str__(self):
#         return self.name
#
#
# class File_type(models.Model):
#     """File_type to be used for fule"""
#     type = models.CharField(max_length=255)
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE
#     )
#
#     def __str__(self):
#         return self.type
#
#
# class User_File(models.Model):
#     """user_files object"""
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE
#     )
#     title = models.CharField(max_length=255)
#     created_on = models.DateTimeField(auto_now_add=True)
#     link = models.CharField(max_length=255, blank=True)
#     file_types = models.ManyToManyField('File_type')
#     tags = models.ManyToManyField('Tag')
#     file = models.FileField(null=True, upload_to=userfile_file_path)
#
#     def __str__(self):
#         return self.title


class User_File(models.Model):
    """user_files object"""
    FILE_TYPE = (
        ('R12', 'DXF R12'),
        ('R13', 'DXF R13'),
        ('R14', 'DXF R14'),
        ('R2000', 'DXF R2000'),
        ('R2004', 'DXF R2004'),
        ('R2007', 'DXF R2007'),
        ('R2010', 'DXF R2010'),
        ('R2013', 'DXF R2013'),
        ('R2018', 'DXF R2018'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=255, blank=True)
    file_types = models.CharField(max_length=14, choices=FILE_TYPE)
    tags = models.CharField(max_length=255, blank=True)
    file = models.FileField(null=True, upload_to=userfile_file_path)

    def __str__(self):
        return self.title
