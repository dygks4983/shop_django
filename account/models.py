from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name="이메일")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="생성일")

    class Meta:
        db_table = "shop_user"
        verbose_name = "계정"
        verbose_name_plural = "계정"
