
from django.db import models

# Create your models here.
class تسجيل_بيروت(models.Model):
    مستوى=[
        ("مبتدئ","مبتدئ"),
        ("قارئ","قارئ"),
        ('حافظ','حافظ'),
        ('مجاز','مجاز'),
    ]
    قراءة = [
        ("تلاوة", "تلاوة"),
        ("قراءات", "قراءات"),
        ('حفظ', 'حفظ'),
    ]
    status=[
        ("اعزب","اعزب"),
        ("متزوج","متزوج"),
        ("منفصل","منفصل"),
    ]
    الاسم_الثلاثي=models.CharField(max_length=200,default=" ")
    الهاتف= models.IntegerField()
    تاريخ_الميلاد = models.CharField(max_length=100)
    العمر = models.IntegerField()
    اسم_الام= models.CharField(max_length=100)
    الجنسية= models.CharField(max_length=100)
    المدرسة_او_الجامعة= models.CharField(max_length=100)
    الصف_او_التخصص= models.CharField(max_length=100)
    التقدير= models.CharField(max_length=100)
    محفوظاته_من_القران = models.CharField(max_length=300,default="0")
    مستوى_القراءة_بالقران=models.CharField(
        max_length=10,
        choices=مستوى,
        default="مبتدئ",
    )
    فئة_الدم=models.CharField
    المستوى_الذي_تود_القراءة_فيه=models.CharField(
        max_length=10,
        choices=قراءة,
        default="حفظ",
    )
    الاوقات_و_الايام_المناسبة_لك=models.CharField
    مكان_السكن_الحالي=models.CharField
    العمل_الحالي=models.CharField
    الوضع_العائلي=models.CharField(
        max_length=10,
        choices=status,
        default="اعزب",
    )
    التاريخ=models.DateTimeField

class تسجيل_طرابلس(models.Model):
    مستوى=[
        ("مبتدئ","مبتدئ"),
        ("قارئ","قارئ"),
        ('حافظ','حافظ'),
        ('مجاز','مجاز'),
    ]
    قراءة = [
        ("تلاوة", "تلاوة"),
        ("قراءات", "قراءات"),
        ('حفظ', 'حفظ'),
    ]
    status=[
        ("اعزب","اعزب"),
        ("متزوج","متزوج"),
        ("منفصل","منفصل"),
    ]
    الاسم_الثلاثي=models.CharField(max_length=200,default=" ")
    الهاتف= models.IntegerField()
    تاريخ_الميلاد = models.CharField(max_length=100)
    العمر = models.IntegerField()
    اسم_الام= models.CharField(max_length=100)
    الجنسية= models.CharField(max_length=100)
    المدرسة_او_الجامعة= models.CharField(max_length=100)
    الصف_او_التخصص= models.CharField(max_length=100)
    التقدير= models.CharField(max_length=100)
    محفوظاته_من_القران = models.CharField(max_length=300,default="0")
    مستوى_القراءة_بالقران=models.CharField(
        max_length=10,
        choices=مستوى,
        default="مبتدئ",
    )
    فئة_الدم=models.CharField
    المستوى_الذي_تود_القراءة_فيه=models.CharField(
        max_length=10,
        choices=قراءة,
        default="حفظ",
    )
    الاوقات_و_الايام_المناسبة_لك=models.CharField
    مكان_السكن_الحالي=models.CharField
    العمل_الحالي=models.CharField
    الوضع_العائلي=models.CharField(
        max_length=10,
        choices=status,
        default="اعزب",
    )
    التاريخ=models.DateField(auto_now=True)

class تسجيل_عكار(models.Model):
    مستوى=[
        ("مبتدئ","مبتدئ"),
        ("قارئ","قارئ"),
        ('حافظ','حافظ'),
        ('مجاز','مجاز'),
    ]
    قراءة = [
        ("تلاوة", "تلاوة"),
        ("قراءات", "قراءات"),
        ('حفظ', 'حفظ'),
    ]
    status=[
        ("اعزب","اعزب"),
        ("متزوج","متزوج"),
        ("منفصل","منفصل"),
    ]
    الاسم_الثلاثي=models.CharField(max_length=200,default=" ")
    الهاتف= models.IntegerField()
    تاريخ_الميلاد = models.CharField(max_length=100)
    العمر = models.IntegerField()
    اسم_الام= models.CharField(max_length=100)
    الجنسية= models.CharField(max_length=100)
    المدرسة_او_الجامعة= models.CharField(max_length=100)
    الصف_او_التخصص= models.CharField(max_length=100)
    التقدير= models.CharField(max_length=100)
    محفوظاته_من_القران = models.CharField(max_length=300,default="0")
    مستوى_القراءة_بالقران=models.CharField(
        max_length=10,
        choices=مستوى,
        default="مبتدئ",
    )
    فئة_الدم=models.CharField
    المستوى_الذي_تود_القراءة_فيه=models.CharField(
        max_length=10,
        choices=قراءة,
        default="حفظ",
    )
    الاوقات_و_الايام_المناسبة_لك=models.CharField
    مكان_السكن_الحالي=models.CharField
    العمل_الحالي=models.CharField
    الوضع_العائلي=models.CharField(
        max_length=10,
        choices=status,
        default="اعزب",
    )
    التاريخ=models.DateField(auto_now=True)

class تسجيل_عرمون(models.Model):
    مستوى=[
        ("مبتدئ","مبتدئ"),
        ("قارئ","قارئ"),
        ('حافظ','حافظ'),
        ('مجاز','مجاز'),
    ]
    قراءة = [
        ("تلاوة", "تلاوة"),
        ("قراءات", "قراءات"),
        ('حفظ', 'حفظ'),
    ]
    status=[
        ("اعزب","اعزب"),
        ("متزوج","متزوج"),
        ("منفصل","منفصل"),
    ]
    الاسم_الثلاثي=models.CharField(max_length=200,default=" ")
    الهاتف= models.IntegerField()
    تاريخ_الميلاد = models.CharField(max_length=100)
    العمر = models.IntegerField()
    اسم_الام= models.CharField(max_length=100)
    الجنسية= models.CharField(max_length=100)
    المدرسة_او_الجامعة= models.CharField(max_length=100)
    الصف_او_التخصص= models.CharField(max_length=100)
    التقدير= models.CharField(max_length=100)
    محفوظاته_من_القران = models.CharField(max_length=300,default="0")
    مستوى_القراءة_بالقران=models.CharField(
        max_length=10,
        choices=مستوى,
        default="مبتدئ",
    )
    فئة_الدم=models.CharField
    المستوى_الذي_تود_القراءة_فيه=models.CharField(
        max_length=10,
        choices=قراءة,
        default="حفظ",
    )
    الاوقات_و_الايام_المناسبة_لك=models.CharField
    مكان_السكن_الحالي=models.CharField
    العمل_الحالي=models.CharField
    الوضع_العائلي=models.CharField(
        max_length=10,
        choices=status,
        default="اعزب",
    )
    التاريخ=models.DateField(auto_now=True)

class تسجيل_صيدا(models.Model):
    مستوى=[
        ("مبتدئ","مبتدئ"),
        ("قارئ","قارئ"),
        ('حافظ','حافظ'),
        ('مجاز','مجاز'),
    ]
    قراءة = [
        ("تلاوة", "تلاوة"),
        ("قراءات", "قراءات"),
        ('حفظ', 'حفظ'),
    ]
    status=[
        ("اعزب","اعزب"),
        ("متزوج","متزوج"),
        ("منفصل","منفصل"),
    ]
    الاسم_الثلاثي=models.CharField(max_length=200,default=" ")
    الهاتف= models.IntegerField()
    تاريخ_الميلاد = models.CharField(max_length=100)
    العمر = models.IntegerField()
    اسم_الام= models.CharField(max_length=100)
    الجنسية= models.CharField(max_length=100)
    المدرسة_او_الجامعة= models.CharField(max_length=100)
    الصف_او_التخصص= models.CharField(max_length=100)
    التقدير= models.CharField(max_length=100)
    محفوظاته_من_القران = models.CharField(max_length=300,default="0")
    مستوى_القراءة_بالقران=models.CharField(
        max_length=10,
        choices=مستوى,
        default="مبتدئ",
    )
    فئة_الدم=models.CharField
    المستوى_الذي_تود_القراءة_فيه=models.CharField(
        max_length=10,
        choices=قراءة,
        default="حفظ",
    )
    الاوقات_و_الايام_المناسبة_لك=models.CharField
    مكان_السكن_الحالي=models.CharField
    العمل_الحالي=models.CharField
    الوضع_العائلي=models.CharField(
        max_length=10,
        choices=status,
        default="اعزب",
    )
    التاريخ=models.DateField(auto_now=True)
