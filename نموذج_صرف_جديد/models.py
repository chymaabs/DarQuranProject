from django.db import models

# Create your models here.
class بيروت(models.Model):
    لامر=models.CharField(max_length=1000,default=" ")
    مبلغ_قدره=models.CharField(max_length=1000,default=" ")
    نقد_او_شيك=models.CharField(max_length=1000,default=" ")
    رقم_الشيك=models.CharField(max_length=1000,default=" ")
    جهةالبنك=models.CharField(max_length=1000,default=" ")
    الموضوع=models.TextField(blank=True, null=True)
    اسم_الحساب=models.CharField(max_length=1000,default=" ")
    المبلغ=models.CharField(max_length=1000,default=" ")
    التاريخ=models.CharField(max_length=1000,default=" ")

class طرابلس(models.Model):
    لامر=models.CharField(max_length=1000,default=" ")
    مبلغ_قدره=models.CharField(max_length=1000,default=" ")
    نقد_او_شيك=models.CharField(max_length=1000,default=" ")
    رقم_الشيك=models.CharField(max_length=1000,default=" ")
    جهةالبنك=models.CharField(max_length=1000,default=" ")
    الموضوع=models.TextField(blank=True, null=True)
    اسم_الحساب=models.CharField(max_length=1000,default=" ")
    المبلغ=models.CharField(max_length=1000,default=" ")
    التاريخ=models.CharField(max_length=1000,default=" ")

class عكار(models.Model):
    لامر=models.CharField(max_length=1000,default=" ")
    مبلغ_قدره=models.CharField(max_length=1000,default=" ")
    نقد_او_شيك=models.CharField(max_length=1000,default=" ")
    رقم_الشيك=models.CharField(max_length=1000,default=" ")
    جهةالبنك=models.CharField(max_length=1000,default=" ")
    الموضوع=models.TextField(blank=True, null=True)
    اسم_الحساب=models.CharField(max_length=1000,default=" ")
    المبلغ=models.CharField(max_length=1000,default=" ")
    التاريخ=models.CharField(max_length=1000,default=" ")

class عرمون(models.Model):
    لامر = models.CharField(max_length=1000, default=" ")
    مبلغ_قدره = models.CharField(max_length=1000, default=" ")
    نقد_او_شيك = models.CharField(max_length=1000, default=" ")
    رقم_الشيك = models.CharField(max_length=1000, default=" ")
    جهةالبنك = models.CharField(max_length=1000, default=" ")
    الموضوع = models.TextField(blank=True, null=True)
    اسم_الحساب = models.CharField(max_length=1000, default=" ")
    المبلغ = models.CharField(max_length=1000, default=" ")
    التاريخ = models.CharField(max_length=1000, default=" ")

class صيدا(models.Model):
    لامر=models.CharField(max_length=1000,default=" ")
    مبلغ_قدره=models.CharField(max_length=1000,default=" ")
    نقد_او_شيك=models.CharField(max_length=1000,default=" ")
    رقم_الشيك=models.CharField(max_length=1000,default=" ")
    جهةالبنك=models.CharField(max_length=1000,default=" ")
    الموضوع=models.TextField(blank=True, null=True)
    اسم_الحساب=models.CharField(max_length=1000,default=" ")
    المبلغ=models.CharField(max_length=1000,default=" ")
    التاريخ=models.CharField(max_length=1000,default=" ")
