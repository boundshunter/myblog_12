from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# 查看文件创建的语句 python manage.py sqlmigrate blog 0001


class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    # related_name 允许通过User反向查询到 BlogArticles
    author = models.ForeignKey(User, on_delete=True, related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        '''定义BlogArticles 显示顺序，按照publish降序'''
        ordering = ("-publish",)

    def __str__(self):
        return self.title

