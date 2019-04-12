from django.shortcuts import render, get_object_or_404, get_list_or_404
from blog import models
# Create your views here.


def blog_title(request):
    blogs = models.BlogArticles.objects.all()
    return render(request, 'blog/titles.html', {"blogs": blogs})


def blog_article(request, article_id):
    '''
    get_object_or_404 简化异常处理，不存在显示404页面
    用法: get_object_or_404(klass, *args, **kwargs)
    klass 是一个model类
    :param request:
    :param article_id: 文章ID
    :return:
    '''
    # article = models.BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(models.BlogArticles, id=article_id)
    return render(request, 'blog/content.html', {"article": article})
