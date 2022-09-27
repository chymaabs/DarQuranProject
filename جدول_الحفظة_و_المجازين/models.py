from django.db import models

# Create your models here.
class بيروت(models.Model):
    اسم_الحافظ=models.CharField(max_length=100)
    الرواية=models.CharField(max_length=100)
    الشيخ_المقرئ=models.CharField(max_length=100)
    المركز=models.CharField(max_length=100)
    لجنة_الاختبار=models.CharField(max_length=100)
    النتيجة=models.CharField(max_length=100)
    التاريخ=models.CharField(max_length=100)
    ملاحظات=models.TextField(blank=True, null=True)

class طرابلس(models.Model):
    اسم_الحافظ=models.CharField(max_length=100)
    الرواية=models.CharField(max_length=100)
    الشيخ_المقرئ=models.CharField(max_length=100)
    المركز=models.CharField(max_length=100)
    لجنة_الاختبار=models.CharField(max_length=100)
    النتيجة=models.CharField(max_length=100)
    التاريخ=models.CharField(max_length=100)
    ملاحظات=models.TextField(blank=True, null=True)
class عكار(models.Model):
    اسم_الحافظ=models.CharField(max_length=100)
    الرواية=models.CharField(max_length=100)
    الشيخ_المقرئ=models.CharField(max_length=100)
    المركز=models.CharField(max_length=100)
    لجنة_الاختبار=models.CharField(max_length=100)
    النتيجة=models.CharField(max_length=100)
    التاريخ=models.CharField(max_length=100)
    ملاحظات=models.TextField(blank=True, null=True)
class عرمون(models.Model):
    اسم_الحافظ=models.CharField(max_length=100)
    الرواية=models.CharField(max_length=100)
    الشيخ_المقرئ=models.CharField(max_length=100)
    المركز=models.CharField(max_length=100)
    لجنة_الاختبار=models.CharField(max_length=100)
    النتيجة=models.CharField(max_length=100)
    التاريخ=models.CharField(max_length=100)
    ملاحظات=models.TextField(blank=True, null=True)
class صيدا(models.Model):
    اسم_الحافظ=models.CharField(max_length=100)
    الرواية=models.CharField(max_length=100)
    الشيخ_المقرئ=models.CharField(max_length=100)
    المركز=models.CharField(max_length=100)
    لجنة_الاختبار=models.CharField(max_length=100)
    النتيجة=models.CharField(max_length=100)
    التاريخ=models.CharField(max_length=100)
    ملاحظات=models.TextField(blank=True, null=True)