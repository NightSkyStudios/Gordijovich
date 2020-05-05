from django.db import models


# Create your models here.
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Project(models.Model):
    name = models.CharField('Назва проекту', max_length=225)
    image = models.ImageField('Фото', upload_to='project_photo', help_text='Картинка що буде обкладинкою роботи')
    url = models.URLField('URL Відео', blank=True, null=True)
    description = models.TextField('Опис проекту')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекти'


class Slider(models.Model):
    video = models.URLField('URL Відео', blank=True, null=True)
    header = models.CharField('Верхній текст', max_length=225)
    footer = models.CharField(max_length=225)

    def __str__(self):
        template = '{0.id} | {0.header}'
        return template.format(self)

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдери'


# Delete photo if model.object delete
@receiver(post_delete)
def submission_delete(sender, instance, **kwargs):
    try:
        instance.image.delete(False)
    except AttributeError:
        pass