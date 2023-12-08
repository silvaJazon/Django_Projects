from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O campo de email é obrigatório.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="Email do Usuário",
        max_length=194,
        unique=True,
    )

    first_name = models.CharField(
        verbose_name="Primeiro Nome",
        max_length=30,
        blank=True,
    )

    last_name = models.CharField(
        verbose_name="Sobrenome",
        max_length=30,
        blank=True,
    )

    is_active = models.BooleanField(
        verbose_name="Usuário está Ativo",
        default=True,
    )

    is_staff = models.BooleanField(
        verbose_name="Usuário é um Dev",
        default=False,
    )

    is_superuser = models.BooleanField(
        verbose_name="Usuario é um SuperUser",
        default=False,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "usuario"

    def __str__(self):
        return f"ID: {self.pk} - {self.email}"
