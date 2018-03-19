from django.db import models

# Create your models here.
class fairytales(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    image=models.ImageField(upload_to='static/img')#Тут будут файлы из базы данных. А в img в проекте будут файлы для самого сайта.
    text=models.TextField(max_length=10000)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Сказка"
        verbose_name_plural="Сказки"