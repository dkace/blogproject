#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


'''
CharField 字符串类型
DateTimeField 时间类型
IntegerField 整数类型
TextField 存储大段文本
'''

'''
分类 Category
标签 Tag
文章 Post
'''

#分类
class Category(models.Model):
    name = models.CharField('栏目分类',max_length=100)

    def __str__(self):
        return self.name

#标签
class Tag(models.Model):
    name = models.CharField('栏目标签',max_length=100)

    def __str__(self):
        return self.name

#文章
class Post(models.Model):
    #标题
    title = models.CharField('栏目标题',max_length=70)
    #正文
    body = models.TextField('文章内容')

    #文章创建时间和最后一次修改时间，存储时间的字段用DateTimeFIled类型
    created_time = models.DateTimeField('文章创建时间')
    modified_time = models.DateTimeField('最后一次修改时间')

    #文章摘要 blank 空白 允许值为true
    excerpt = models.CharField('文章摘要',max_length=200,blank=True)

    #分类与标模型已定义在上面
    #在下面吧文章对应的数据库表和分类，标签对应的数据库表关联了起来
    #文章对应一个分类，一个分类可以有多篇文章，所以是一对多的关系，使用 Foreignkey
    #对于标签来说，一篇文章可以有多个标签，同一个标签下有可能有多篇文章，所以是多对多的关系，使用manyToManyField

    category = models.ForeignKey(Category,on_delete='none')
    tag = models.ManyToManyField(Tag,blank=True)

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。

    author = models.ForeignKey(User,on_delete='none')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-created_time']
