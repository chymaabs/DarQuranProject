from django.db import models

# Create your models here.
class بيروت(models.Model):
     اسم_المدرس=models.CharField(max_length=1000,default=" ")
     اسم_الطالب=models.CharField(max_length=1000,default=" ")
     تاريخ_بدء_برنامج_الضبط=models.CharField(max_length=1000,default=" ")
     المدة=models.CharField(max_length=1000,default=" ")
     الرواية=models.CharField(max_length=1000,default=" ")
     تاريخ_الاختبار=models.CharField(max_length=1000,default=" ")
     من_الى=models.CharField(max_length=1000,default=" ")
     التقدير=models.CharField(max_length=1000,default=" ")
     ملاحظات=models.TextField(blank=True, null=True)

class طرابلس(models.Model):
     اسم_المدرس = models.CharField(max_length=1000, default=" ")
     اسم_الطالب = models.CharField(max_length=1000, default=" ")
     تاريخ_بدء_برنامج_الضبط = models.CharField(max_length=1000, default=" ")
     المدة = models.CharField(max_length=1000, default=" ")
     الرواية = models.CharField(max_length=1000, default=" ")
     تاريخ_الاختبار = models.CharField(max_length=1000, default=" ")
     من_الى = models.CharField(max_length=1000, default=" ")
     التقدير = models.CharField(max_length=1000, default=" ")
     ملاحظات = models.TextField(blank=True, null=True)

class عكار(models.Model):
     اسم_المدرس = models.CharField(max_length=1000, default=" ")
     اسم_الطالب = models.CharField(max_length=1000, default=" ")
     تاريخ_بدء_برنامج_الضبط = models.CharField(max_length=1000, default=" ")
     المدة = models.CharField(max_length=1000, default=" ")
     الرواية = models.CharField(max_length=1000, default=" ")
     تاريخ_الاختبار = models.CharField(max_length=1000, default=" ")
     من_الى = models.CharField(max_length=1000, default=" ")
     التقدير = models.CharField(max_length=1000, default=" ")
     ملاحظات = models.TextField(blank=True, null=True)

class عرمون(models.Model):
     اسم_المدرس = models.CharField(max_length=1000, default=" ")
     اسم_الطالب = models.CharField(max_length=1000, default=" ")
     تاريخ_بدء_برنامج_الضبط = models.CharField(max_length=1000, default=" ")
     المدة = models.CharField(max_length=1000, default=" ")
     الرواية = models.CharField(max_length=1000, default=" ")
     تاريخ_الاختبار = models.CharField(max_length=1000, default=" ")
     من_الى = models.CharField(max_length=1000, default=" ")
     التقدير = models.CharField(max_length=1000, default=" ")
     ملاحظات = models.TextField(blank=True, null=True)

class صيدا(models.Model):
     اسم_المدرس = models.CharField(max_length=1000, default=" ")
     اسم_الطالب = models.CharField(max_length=1000, default=" ")
     تاريخ_بدء_برنامج_الضبط = models.CharField(max_length=1000, default=" ")
     المدة = models.CharField(max_length=1000, default=" ")
     الرواية = models.CharField(max_length=1000, default=" ")
     تاريخ_الاختبار = models.CharField(max_length=1000, default=" ")
     من_الى = models.CharField(max_length=1000, default=" ")
     التقدير = models.CharField(max_length=1000, default=" ")
     ملاحظات = models.TextField(blank=True, null=True)
