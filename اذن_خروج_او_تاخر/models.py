from django.db import models

from django.db import models


# Create your models here.
class بيروت(models.Model):
    اليوم = models.CharField(max_length=1000)
    القسم = models.CharField(max_length=1000,default=" ")
    التاريخ = models.CharField(max_length=1000)
    البديل = models.CharField(max_length=1000)
    اسم_الموظف= models.CharField(max_length=1000)
    سبب_الخروج = models.CharField(max_length=1000,default=" ")
    اذن_خروج_خلالالعمل_من_الى = models.CharField(max_length=1000,default="-")
    اذن_للتأخر_عن_العمل_من_الى = models.CharField(max_length=1000,default="-")
    اذن_خروج_لترك_العمل_من_الى = models.CharField(max_length=1000,default="-")
    عدد_الساعات = models.IntegerField()

class طرابلس(models.Model):
    اليوم = models.CharField(max_length=1000)
    القسم = models.CharField(max_length=1000,default=" ")
    التاريخ = models.CharField(max_length=1000)
    البديل = models.CharField(max_length=1000)
    اسم_الموظف= models.CharField(max_length=1000)
    سبب_الخروج = models.CharField(max_length=1000,default=" ")
    اذن_خروج_خلالالعمل_من_الى = models.CharField(max_length=1000,default="-")
    اذن_للتأخر_عن_العمل_من_الى = models.CharField(max_length=1000,default="-")
    اذن_خروج_لترك_العمل_من_الى = models.CharField(max_length=1000,default="-")
    عدد_الساعات = models.IntegerField()


class عكار(models.Model):
    اليوم = models.CharField(max_length=1000)
    القسم = models.CharField(max_length=1000,default=" ")
    التاريخ = models.CharField(max_length=1000)
    البديل = models.CharField(max_length=1000)
    اسم_الموظف= models.CharField(max_length=1000)
    سبب_الخروج = models.CharField(max_length=1000,default=" ")
    اذن_خروج_خلالالعمل_من_الى = models.CharField(max_length=1000,default="-")
    اذن_للتأخر_عن_العمل_من_الى = models.CharField(max_length=1000,default="-")
    اذن_خروج_لترك_العمل_من_الى = models.CharField(max_length=1000,default="-")
    عدد_الساعات = models.IntegerField()


class عرمون(models.Model):
    اليوم = models.CharField(max_length=1000)
    القسم = models.CharField(max_length=1000,default=" ")
    التاريخ = models.CharField(max_length=1000)
    البديل = models.CharField(max_length=1000)
    اسم_الموظف= models.CharField(max_length=1000)
    سبب_الخروج = models.CharField(max_length=1000,default=" ")
    اذن_خروج_خلالالعمل_من_الى = models.CharField(max_length=1000,default="-")
    اذن_للتأخر_عن_العمل_من_الى = models.CharField(max_length=1000,default="-")
    اذن_خروج_لترك_العمل_من_الى = models.CharField(max_length=1000,default="-")
    عدد_الساعات = models.IntegerField()


class صيدا(models.Model):
    اليوم = models.CharField(max_length=1000)
    القسم = models.CharField(max_length=1000,default=" ")
    التاريخ = models.CharField(max_length=1000)
    البديل = models.CharField(max_length=1000)
    اسم_الموظف= models.CharField(max_length=1000)
    سبب_الخروج = models.CharField(max_length=1000,default=" ")
    اذن_خروج_خلالالعمل_من_الى = models.CharField(max_length=1000,default="-")
    اذن_للتأخر_عن_العمل_من_الى = models.CharField(max_length=1000,default="-")
    اذن_خروج_لترك_العمل_من_الى = models.CharField(max_length=1000,default="-")
    عدد_الساعات = models.IntegerField()
