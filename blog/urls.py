from django.urls import path
from blog import views
from django.contrib.staticfiles.views import serve
from django.views.generic.base import RedirectView
urlpatterns = [
    #首页
    path('', views.index,name='index'),
    #文章详情页
    path('article/<int:id>/',views.article_detail,name='article_detail'),
    #成员页
    path('member/',views.member,name='member'),
    #分类和标签页
    path('category_tag/',views.category_tag,name='category_tag'),
    #文章分类详情页
    path('article_category/(?P<id>[0-9]+)$',views.article_category,name='article_category'),
    #文章标签详情页
    path('article_tag/<int:id>',views.article_tag,name='article_tag'),
    #关于
    path('about/', views.about, name='about'),
    #path('favicon.ico', serve, {'path': 'static/img/favicon.ico'}),
    #path('favicon.ico', RedirectView.as_view(url='static/img/favicon.ico')),
]

#mkeditor配置
from django.conf.urls.static import static
from django.conf import settings
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)