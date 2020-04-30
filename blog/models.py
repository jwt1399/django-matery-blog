from django.db import models
from datetime import datetime
from django.utils.html import format_html
from mdeditor.fields import MDTextField
class Category(models.Model):
    '''文章分类'''
    name = models.CharField(max_length=20, verbose_name='分类名称')
    index = models.IntegerField(default=1, verbose_name='分类排序')
    add_menu = models.BooleanField(default=False, verbose_name='添加到导航栏')
    icon = models.CharField(max_length=30, default='fas fa-home',verbose_name='导航图标')
    class Meta:
        verbose_name_plural=verbose_name = '分类'

    #统计分类对应文章数,并放入后台
    def get_items(self):
        return len(self.article_set.all())
    get_items.short_description = '文章数'  # 设置后台显示表头
    #后台图标预览
    def icon_data(self):#引入Font Awesome Free 5.11.1
        return format_html('<h1><i class="{}"></i></h1>',self.icon) #转化为<i class="{self.icon}"></i>
    icon_data.short_description = '图标预览'
    def __str__(self):
        return self.name

class Tag(models.Model):
    '''标签'''
    name = models.CharField(max_length=20, verbose_name='标签名称')
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    # 统计分类对应文章数,并放入后台
    def get_items(self):
        return len(self.article_set.all())
    get_items.short_description = '文章数'  # 设置后台显示表头
    def __str__(self):
        return self.name

class Article(models.Model):
    '''文章'''
    title = models.CharField(max_length=50, verbose_name='文章标题')
    author = models.CharField(max_length=10, verbose_name='作者',default='简文涛',blank=True,null=True)
    desc = models.CharField(max_length=50, verbose_name='文章描述')
    cover = models.URLField(max_length=200, default='https://i.loli.net/2020/04/23/lJLjEtbs2NFwynQ.jpg', verbose_name='文章封面')
    content = MDTextField(verbose_name='文章内容')
    click_count = models.PositiveIntegerField(default=0, verbose_name='阅读量')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    # 文章创建时间。参数 default=datetime.now 指定其在创建数据时将默认写入当前的时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    # 文章更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='文章分类', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag,blank=True, verbose_name='文章标签')
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ('-add_time',) #以创建时间倒序排列
    def cover_preview(self):
        return format_html('<img src="{}" width="200px" height="150px"/>',self.cover,)
    cover_preview.short_description = '文章封面预览'

    def __str__(self):
        return self.title    #将文章标题返回

class Link(models.Model):
    '''成员'''
    title = models.CharField(max_length=10,verbose_name='标题')
    url = models.URLField(verbose_name='网址',blank=True)
    avatar = models.URLField(default='https://i.loli.net/2020/04/23/jGP8gQOYW75TSJp.png',verbose_name='头像')
    desc = models.TextField(max_length=50,verbose_name='描述')
    button_word =models.CharField(default='访问博客',max_length=10,verbose_name='跳转文字')
    class Meta:
        verbose_name=verbose_name_plural='成员'
    #后台头像预览
    def avatar_admin(self):
        return format_html( '<img src="{}" width="50px" height="50px" style="border-radius: 50%;" />',self.avatar,)
    avatar_admin.short_description = '头像预览'
    def __str__(self):
        return self.title

class Notice(models.Model):
    '''公告栏'''
    title = models.CharField(max_length=30,verbose_name='公告栏标题')
    content = models.TextField(max_length=500,verbose_name='公告内容')
    icon = models.CharField(default='far fa-lightbulb',max_length=50,verbose_name='公告图标')
    class Meta:
        verbose_name=verbose_name_plural='公告栏'
    def icon_data(self):
        return format_html('<h1><i class="{}"></i></h1>',self.icon) #转化为<i class="{self.icon}"></i>
    icon_data.short_description = '图标预览'
    def __str__(self):
        return self.title

class Valine(models.Model):
    '''valine评论'''
    appid = models.CharField(max_length=100,verbose_name='appId')
    appkey = models.CharField(max_length=100, verbose_name='appKey')
    avatar = models.CharField(default='',blank=True,max_length=100, verbose_name='avatar')
    pagesize = models.IntegerField(default='10',verbose_name='pageSize')
    placeholder = models.CharField(max_length=100, verbose_name='placeholder')
    class Meta:
        verbose_name = 'valine评论'
        verbose_name_plural = verbose_name

class About(models.Model):
    '''关于'''
    avatar = models.URLField(verbose_name='头像')
    career = models.CharField(max_length=50,verbose_name='事业')
    introduction = models.TextField(verbose_name='介绍')
    skill_title = models.CharField(default='技能',max_length=50, verbose_name='技能标题')
    class Meta:
        verbose_name_plural = verbose_name = '关于'
    def avatar_admin(self):
        return format_html( '<img src="{}" width="50px" height="50px" style="border-radius: 50%;" />',self.avatar,)
    avatar_admin.short_description = '头像预览'

class Social(models.Model):
    '''社交链接'''
    social_url = models.URLField(verbose_name='社交链接')
    social_desc = models.CharField(max_length=50,verbose_name='简介')
    social_icon =models.CharField(max_length=50, default='fas fa-envelope', verbose_name='社交图标')
    class Meta:
        verbose_name_plural = verbose_name = '社交'
    # 后台图标预览
    def icon_data(self):
        return format_html('<h1><i class="{}"></i></h1>', self.social_icon)
    icon_data.short_description = '图标预览'
class Skill(models.Model):
    '''关于页技能'''
    skill_name = models.CharField(max_length=50,verbose_name='方向名')
    skill_precent =models.CharField(default='%',max_length=50,verbose_name='百分比')
    class Meta:
        verbose_name_plural = verbose_name = '技能'
    # 后台图标预览
    def icon_data(self):
        return format_html('<h1><i class="{}"></i></h1>', self.social_icon)
    icon_data.short_description = '图标预览'

class Site(models.Model):
    """站点配置"""
    site_name = models.CharField(default='简简',max_length=30,verbose_name='网站名字')
    keywords = models.CharField(default='关键字测试',max_length=50, verbose_name='网站关键词')
    logo = models.URLField(default='https://jwt1399.top/favicon.png',max_length=100, verbose_name='网站logo')
    desc = models.CharField(max_length=50, verbose_name='网站描述')
    slogan = models.CharField(max_length=50, verbose_name='网站标语')
    dynamic_slogan = models.CharField(max_length=50, verbose_name='动态标语')
    icp_number = models.CharField(max_length=40, verbose_name='备案号')
    icp_url = models.URLField(default='http://www.beian.miit.gov.cn/',max_length=100, verbose_name='备案链接')
    bg_cover = models.URLField(default='http://119.23.243.154/image/Covteam-hack.jpg',max_length=100,verbose_name='背景图片')


    class Meta:
        verbose_name = '网站设置'
        verbose_name_plural = verbose_name
    def logo_preview(self):#logo预览
        return format_html('<img src="{}" width="40px" height="40px" alt="logo" />',self.logo)
    logo_preview.short_description = 'logo预览'
    def bgcover_preview(self):#背景图片预览
        return format_html('<img src="{}" width="100px" height="80px" alt="bgcover" />',self.bg_cover)
    bgcover_preview.short_description = '首页背景预览'
    def __str__(self):
        return self.site_name


