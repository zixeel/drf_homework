from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='почта')
    username = None
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=35, verbose_name='country', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Payment(models.Model):
    PAYMENT_METHOD = (
        ('CASH', 'cash'),
        ('CASHLESS', 'cashless')
    )

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='пользователь')
    pay_day = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    paid_course = models.ForeignKey('materials.Course', on_delete=models.SET_NULL, verbose_name='оплаченный курс',
                                    **NULLABLE)
    payment_amount = models.IntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(verbose_name='способ оплаты', choices=PAYMENT_METHOD)
