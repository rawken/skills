from django.db import models
import os
from django.conf import settings

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

def project_directory_path(instance, filename):

    return '{0}/{1}'.format(instance.main_title, filename)

# Create your models here.
class Project(models.Model):
    main_title = models.CharField('Название проекта', max_length=200, unique=True)
    cover_img = models.ImageField('Обложка проекта', upload_to=project_directory_path)
    cover_text = models.CharField('Текст на обложке (необязательно)', max_length=200, blank=True)
    first_title = models.CharField('Первый заголовок', max_length=200)
    main_description = models.TextField('Описание проекта')
    pub_date = models.DateTimeField('Дата публикации')
 #   project_images = models.ImageField(upload_to=project_directory_path)
    second_title = models.CharField('Второй заголовок (необязателен)', max_length=200, blank=True)
    second_description = models.TextField('Второе описание (необязательно)', blank=True)
    video_url = models.URLField('Ссылка на видео проекта (необязательно)', blank=True)

    def __str__(self):
        return self.main_title

class ProjectImages(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=project_directory_path)

    def __str__(self):
        return self.project.main_title