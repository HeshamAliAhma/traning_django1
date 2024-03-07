from django.db import models

from django.contrib.auth.models import User

# from django.utils import timezone



# Create your models here.

class Post(models.Model):

    class POSTTYPE_CHOICES(models.TextChoices):
        Question = 'question','سؤال'
        POST = 'post','منشور'
        ARTICLE = 'article','مقال'

    class Status(models.TextChoices):
        DRAFT = 'DF','Draft'
        PUBLISHED = 'PB','published'
    
    type_post = models.CharField( max_length=10 , choices = POSTTYPE_CHOICES.choices,default=POSTTYPE_CHOICES.POST , verbose_name = "نوع المنشور")
    title_post = models.CharField(max_length=250, verbose_name = "عنوان المنشور")
    slug_post = models.SlugField(max_length=250,verbose_name= "اللينك", unique='True')
    author = models.ForeignKey(User, verbose_name="صاحب المنشور", on_delete=models.CASCADE)
    body = models.TextField(max_length=500 , verbose_name="محتوي المنشور")   

    status = models.CharField(max_length=2 , choices = Status.choices,default=Status.DRAFT,verbose_name='حالة المنشور')


    class Meta():
        verbose_name = "منشور"
        verbose_name_plural = "منشورات" 
        # ordering = ['-publish']
        # indexes = [
        #     models.Index(fields=['-publish']),
        # ]


    def __str__(self):
        return self.title_post