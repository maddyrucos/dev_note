from django.contrib.auth import get_user_model
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_created=True, blank=True, null=True, default=None)
    last_updated = models.DateTimeField(auto_now=True)
    git_hub_url = models.URLField(null=True, blank=True)
    deploy_url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title



class Note(models.Model):
    id = models.AutoField(primary_key=True)
    #project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
