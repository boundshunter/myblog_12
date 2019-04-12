from django.contrib import admin
from .models import BlogArticles # blogarticles引入
# Register your models here.
# admin.site.register(BlogArticles) # BlogArticles 注册到admin


class BlogArticlesAdmin(admin.ModelAdmin):
        list_display = ("title", "author", "publish")
        list_filter = ("publish", "author")
        search_fields = ("title", "body")
        raw_id_fields = ("author",)
        date_hierarchy = "publish"
        order = ["publish", "author"]
admin.site.register(BlogArticles, BlogArticlesAdmin)
