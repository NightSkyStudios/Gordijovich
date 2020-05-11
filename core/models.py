from django.db import models

# Create your models here.
from django.db.models.signals import post_delete
from django.dispatch import receiver
from autoslug import AutoSlugField


class Project(models.Model):
    name = models.CharField('Назва проекту', max_length=225)
    image = models.ImageField('Фото', upload_to='project_photo', help_text='Картинка що буде обкладинкою роботи')
    url = models.URLField('URL Відео', blank=True, null=True)
    description = models.TextField('Опис проекту')
    slug = AutoSlugField(populate_from='name')
    is_hidden = models.BooleanField('Приховати публікацію', default=False ,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекти'


class Partner(models.Model):
    image = models.ImageField('Зображення', upload_to='partners')
    name = models.CharField('Назва', max_length=125)
    link = models.URLField('Посилання')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнери'


# Delete photo if model.object delete
@receiver(post_delete)
def submission_delete(sender, instance, **kwargs):
    try:
        instance.image.delete(False)
    except AttributeError:
        pass
