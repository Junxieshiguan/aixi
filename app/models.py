from django.db import models

# Create your models here.
class Recommend(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

    # 将父类定义为抽象类（不会创建表）
    class Meta:
        abstract = True

class Wheel(Recommend):
    class Meta:
        db_table = 'axf_wheel'


class Nav(Recommend):
    class Meta:
        db_table='axf_nav'

class Mustbuy(Recommend):
    class Meta:
        db_table = 'axf_mustbuy'

class Shop(Recommend):
    class Meta:
        db_table = 'axf_shop'
