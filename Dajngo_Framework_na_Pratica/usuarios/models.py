from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="Email do Usuário",
        max_length=194,
        unique=True,
    )

    is_active = models.BooleanField(
        verbose_name="Usuário está Ativo",
        default=True,
    )

    is_staff = models.BooleanField(
        verbose_name="Usuário e um Dev",
        default=False,
    )

    is_superuser = models.BooleanField(
        verbose_name="Usuario é um Superuser",
        default=False,
    )

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "Usuário",
        verbose_name_plural = "Usuários"
        db_table = "usuario"

    def __str__(self):
        return self.email
