from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        user = self.model(
            email=self.normalize_email(email)
        )

        user.is_active = True
        user.is_staff = False
        user.is_superuser = False

        if password:
            user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.set_password(password)

        user.save()

        def get_active_users(self):
            return self.get_queryset().filter(is_active=True)


class User(AbstractBaseUser, PermissionsMixin):
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
