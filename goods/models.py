from django.db import models
from django.utils import timezone

class GoodsGroup(models.Model):
    name = models.CharField(verbose_name='商品グループ', unique=True, max_length=15, null=True)

    def __str__(self):
        return self.name

class GoodsCreate(models.Model):
    name = models.CharField(verbose_name='商品名', max_length=200, unique=True)
    price = models.IntegerField(verbose_name='価格', blank=False)
    release_date = models.DateField(verbose_name='発売日', default=timezone.now)
    description = models.CharField(verbose_name='説明', max_length=10000)
    image = models.ImageField(verbose_name='画像', null=True, blank=True, upload_to='images/')

    #TODO:null=True,blank=Trueを追加。
    group = models.ForeignKey(GoodsGroup, on_delete=models.CASCADE, verbose_name='商品グループ',null=True,blank=True)

    def __str__(self):
        return self.name
