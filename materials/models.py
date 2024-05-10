from django.db import models

from users.models import NULLABLE


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='навзвание')
    description = models.TextField(verbose_name='описание')
    pre_view = models.ImageField(upload_to='lesson/', verbose_name='превью', **NULLABLE)
    video_url = models.URLField(verbose_name='ссыока на видео', **NULLABLE)
    course = models.ForeignKey('materials.Course', on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    pre_view = models.ImageField(upload_to='course/', verbose_name='превью ', **NULLABLE)

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('name',)
