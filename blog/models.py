from django.db import models

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Дата публикации')
    #cover_img = 