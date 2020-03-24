from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

<<<<<<< HEAD

class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, muses=0, gender=2, **extra_fields):
=======
from arts.models import Art

class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, gender=2, **extra_fields):
>>>>>>> a0abb14f89ddca52fedf33fe1dec85686c1b26d8
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
<<<<<<< HEAD
        user = self.model(email=email, username=username,  gender=gender,**extra_fields)
=======
        user = self.model(email=email, username=username, gender=gender, muses=0, caught_arts=[], **extra_fields)
>>>>>>> a0abb14f89ddca52fedf33fe1dec85686c1b26d8
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, gender, username='', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
<<<<<<< HEAD
        return self._create_user(email, gender, username, muses, password, **extra_fields)
=======
        return self._create_user(email, gender, username, password, **extra_fields)
>>>>>>> a0abb14f89ddca52fedf33fe1dec85686c1b26d8

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, 'blogs/like_section.html',  password, **extra_fields)

<<<<<<< HEAD
GENDER_CHOICES = [
    (0, 'Male'),
    (1, 'Female'),
    (2, 'Not to disclose')
]

=======
>>>>>>> a0abb14f89ddca52fedf33fe1dec85686c1b26d8
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=255, verbose_name="이메일", unique=True)
    username = models.CharField(max_length=64, verbose_name="사용자명")
    gender = models.SmallIntegerField(choices=GENDER_CHOICES)
<<<<<<< HEAD
    caught_posts = models.IntegerField()
=======
    caught_arts = models.ForeignKey(Art, on_delete=models.CASCADE)
>>>>>>> a0abb14f89ddca52fedf33fe1dec85686c1b26d8
    muses = models.IntegerField()
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
<<<<<<< HEAD
        return "<%d %s>" % (self.pk, self.email)
=======
        return "<%d %s>" % (self.pk, self.email)
>>>>>>> a0abb14f89ddca52fedf33fe1dec85686c1b26d8
