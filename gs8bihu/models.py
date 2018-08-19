from django.db import models

# Create your models here.


class RecommendAuthor(models.Model):
    id = models.IntegerField(u'用户ID', primary_key=True)
    name = models.CharField(u'用户名', max_length=20)
    info = models.CharField(u'自我介绍', max_length=100)
    icon = models.CharField(u'图标', max_length=100)
    artnum = models.IntegerField(u'文章数量')
    fans = models.IntegerField(u'粉丝数')
    order = models.IntegerField(u'排序')

    def __unicode__(self):
        return self.name

    class Meta:  # 按时间下降排序
        ordering = ['-order']
        verbose_name = "文章"
        verbose_name_plural = "文章"
