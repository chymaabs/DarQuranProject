from django.db import models

# Create your models here.
status = [
    ("اعزب", "اعزب"),
    ("متزوج", "متزوج"),
    ("منفصل", "منفصل"),
]
اجازة=[
    ("مجاز","مجاز"),
    ('غير مجاز','غير مجاز'),
]
cost=[
    ("ببدل",'ببدل'),
    ('تطوع','تطوع'),
]
age=[
    ('كبار','كبار'),
    ('صغار',"صغار"),
]

class بيروت(models.Model):
    الاسم_الثلاثي=models.CharField(max_length=200,default=" ")
    الهاتف= models.IntegerField()
    تاريخ_الميلاد = models.CharField(max_length=1000,default=" ")
    العمل_الحالي=models.TextField(blank=True, null=True)
    مكان_الاقامة=models.TextField(blank=True, null=True)
    المعرف=models.TextField(blank=True, null=True)
    الوضع_العائلي = models.CharField(
        max_length=10,
        choices=status,
        default="اعزب",
    )
    التاريخ = models.TextField(blank=True, null=True)
    المدرسة_او_الجامعة = models.CharField(max_length=1000,default=" ")
    الصف_او_التخصص = models.CharField(max_length=1000,default=" ")
    شهادات_اخرى=models.TextField(blank=True, null=True)
    الاجزاء_المحفوظة=models.TextField(blank=True, null=True)
    مجاز= models.CharField(
        max_length=10,
        choices=اجازة,
        default="غير مجاز",
    )

    الشيخ_المجيز=models.TextField(blank=True, null=True)
    الرواية=models.TextField(blank=True, null=True)
    روايات_اخرى=models.TextField(blank=True, null=True)
    الشيخ_المجيز=models.TextField(blank=True, null=True)
    علوم_القرآن_و_التفسير= models.CharField(max_length=1000)
    الكتاب= models.CharField(max_length=1000,default=" ")
    الشيخ_الذي_قرأت_عليه= models.CharField(max_length=1000,default=" ")
    العقيدة= models.CharField(max_length=1000,default=" ")
    الكتاب= models.CharField(max_length=1000,default=" ")
    الشيخ_الذي_قرأت_عليه= models.CharField(max_length=1000,default=" ")
    النحو= models.CharField(max_length=10000,default=" ")
    الكتاب= models.CharField(max_length=1000,default=" ")
    الشيخ_الذي_قرأت_عليه= models.CharField(max_length=1000,default=" ")
    ترغب_بالتدريس=models.CharField(
        max_length=10,
        choices=cost,
        default="ببدل",
    )
    الفئة_العمرية=  models.CharField(
        max_length=10,
        choices=age,
        default="كبار",
    )
    الاوقات_و_الايام_المناسبة_لك=models.CharField
    رأي_اللجنة_العلمية=models.CharField(max_length=1000,default=" ")
    قرار_الادارة=models.CharField(max_length=1000,default=" ")








class طرابلس(models.Model):
    الاسم_الثلاثي = models.CharField(max_length=200, default=" ")
    الهاتف = models.IntegerField()
    تاريخ_الميلاد = models.CharField(max_length=1000, default=" ")
    العمل_الحالي = models.TextField(blank=True, null=True)
    مكان_الاقامة = models.TextField(blank=True, null=True)
    المعرف = models.TextField(blank=True, null=True)
    الوضع_العائلي = models.CharField(
        max_length=10,
        choices=status,
        default="اعزب",
    )
    التاريخ = models.TextField(blank=True, null=True)
    المدرسة_او_الجامعة = models.CharField(max_length=1000, default=" ")
    الصف_او_التخصص = models.CharField(max_length=1000, default=" ")
    شهادات_اخرى = models.TextField(blank=True, null=True)
    الاجزاء_المحفوظة = models.TextField(blank=True, null=True)
    مجاز = models.CharField(
        max_length=10,
        choices=اجازة,
        default="غير مجاز",
    )

    الشيخ_المجيز = models.TextField(blank=True, null=True)
    الرواية = models.TextField(blank=True, null=True)
    روايات_اخرى = models.TextField(blank=True, null=True)
    الشيخ_المجيز = models.TextField(blank=True, null=True)
    علوم_القرآن_و_التفسير = models.CharField(max_length=1000)
    الكتاب = models.CharField(max_length=1000, default=" ")
    الشيخ_الذي_قرأت_عليه = models.CharField(max_length=1000, default=" ")
    العقيدة = models.CharField(max_length=1000, default=" ")
    الكتاب = models.CharField(max_length=1000, default=" ")
    الشيخ_الذي_قرأت_عليه = models.CharField(max_length=1000, default=" ")
    النحو = models.CharField(max_length=10000, default=" ")
    الكتاب = models.CharField(max_length=1000, default=" ")
    الشيخ_الذي_قرأت_عليه = models.CharField(max_length=1000, default=" ")
    ترغب_بالتدريس = models.CharField(
        max_length=10,
        choices=cost,
        default="ببدل",
    )
    الفئة_العمرية = models.CharField(
        max_length=10,
        choices=age,
        default="كبار",
    )
    الاوقات_و_الايام_المناسبة_لك = models.CharField
    رأي_اللجنة_العلمية = models.CharField(max_length=1000, default=" ")
    قرار_الادارة = models.CharField(max_length=1000, default=" ")


class عكار(models.Model):
    الاسم_الثلاثي = models.CharField(max_length=200, default=" ")
    الهاتف = models.IntegerField()
    تاريخ_الميلاد = models.CharField(max_length=1000, default=" ")
    العمل_الحالي = models.TextField(blank=True, null=True)
    مكان_الاقامة = models.TextField(blank=True, null=True)
    المعرف = models.TextField(blank=True, null=True)
    الوضع_العائلي = models.CharField(
        max_length=10,
        choices=status,
        default="اعزب",
    )
    التاريخ = models.TextField(blank=True, null=True)
    المدرسة_او_الجامعة = models.CharField(max_length=1000, default=" ")
    الصف_او_التخصص = models.CharField(max_length=1000, default=" ")
    شهادات_اخرى = models.TextField(blank=True, null=True)
    الاجزاء_المحفوظة = models.TextField(blank=True, null=True)
    مجاز = models.CharField(
        max_length=10,
        choices=اجازة,
        default="غير مجاز",
    )

    الشيخ_المجيز = models.TextField(blank=True, null=True)
    الرواية = models.TextField(blank=True, null=True)
    روايات_اخرى = models.TextField(blank=True, null=True)
    الشيخ_المجيز = models.TextField(blank=True, null=True)
    علوم_القرآن_و_التفسير = models.CharField(max_length=1000)
    الكتاب = models.CharField(max_length=1000, default=" ")
    الشيخ_الذي_قرأت_عليه = models.CharField(max_length=1000, default=" ")
    العقيدة = models.CharField(max_length=1000, default=" ")
    الكتاب = models.CharField(max_length=1000, default=" ")
    الشيخ_الذي_قرأت_عليه = models.CharField(max_length=1000, default=" ")
    النحو = models.CharField(max_length=10000, default=" ")
    الكتاب = models.CharField(max_length=1000, default=" ")
    الشيخ_الذي_قرأت_عليه = models.CharField(max_length=1000, default=" ")
    ترغب_بالتدريس = models.CharField(
        max_length=10,
        choices=cost,
        default="ببدل",
    )
    الفئة_العمرية = models.CharField(
        max_length=10,
        choices=age,
        default="كبار",
    )
    الاوقات_و_الايام_المناسبة_لك = models.CharField
    رأي_اللجنة_العلمية = models.CharField(max_length=1000, default=" ")
    قرار_الادارة = models.CharField(max_length=1000, default=" ")


class عرمون(models.Model):
    الاسم_الثلاثي = models.CharField(max_length=200, default=" ")
    الهاتف = models.IntegerField()
    تاريخ_الميلاد = models.CharField(max_length=1000, default=" ")
    العمل_الحالي = models.TextField(blank=True, null=True)
    مكان_الاقامة = models.TextField(blank=True, null=True)
    المعرف = models.TextField(blank=True, null=True)
    الوضع_العائلي = models.CharField(
        max_length=10,
        choices=status,
        default="اعزب",
    )
    التاريخ = models.TextField(blank=True, null=True)
    المدرسة_او_الجامعة = models.CharField(max_length=1000, default=" ")
    الصف_او_التخصص = models.CharField(max_length=1000, default=" ")
    شهادات_اخرى = models.TextField(blank=True, null=True)
    الاجزاء_المحفوظة = models.TextField(blank=True, null=True)
    مجاز = models.CharField(
        max_length=10,
        choices=اجازة,
        default="غير مجاز",
    )

    الشيخ_المجيز = models.TextField(blank=True, null=True)
    الرواية = models.TextField(blank=True, null=True)
    روايات_اخرى = models.TextField(blank=True, null=True)
    الشيخ_المجيز = models.TextField(blank=True, null=True)
    علوم_القرآن_و_التفسير = models.CharField(max_length=1000)
    الكتاب = models.CharField(max_length=1000, default=" ")
    الشيخ_الذي_قرأت_عليه = models.CharField(max_length=1000, default=" ")
    العقيدة = models.CharField(max_length=1000, default=" ")
    الكتاب = models.CharField(max_length=1000, default=" ")
    الشيخ_الذي_قرأت_عليه = models.CharField(max_length=1000, default=" ")
    النحو = models.CharField(max_length=10000, default=" ")
    الكتاب = models.CharField(max_length=1000, default=" ")
    الشيخ_الذي_قرأت_عليه = models.CharField(max_length=1000, default=" ")
    ترغب_بالتدريس = models.CharField(
        max_length=10,
        choices=cost,
        default="ببدل",
    )
    الفئة_العمرية = models.CharField(
        max_length=10,
        choices=age,
        default="كبار",
    )
    الاوقات_و_الايام_المناسبة_لك = models.CharField
    رأي_اللجنة_العلمية = models.CharField(max_length=1000, default=" ")
    قرار_الادارة = models.CharField(max_length=1000, default=" ")


class صيدا(models.Model):
    الاسم_الثلاثي = models.CharField(max_length=200, default=" ")
    الهاتف = models.IntegerField()
    تاريخ_الميلاد = models.CharField(max_length=1000, default=" ")
    العمل_الحالي = models.TextField(blank=True, null=True)
    مكان_الاقامة = models.TextField(blank=True, null=True)
    المعرف = models.TextField(blank=True, null=True)
    الوضع_العائلي = models.CharField(
        max_length=10,
        choices=status,
        default="اعزب",
    )
    التاريخ = models.TextField(blank=True, null=True)
    المدرسة_او_الجامعة = models.CharField(max_length=1000, default=" ")
    الصف_او_التخصص = models.CharField(max_length=1000, default=" ")
    شهادات_اخرى = models.TextField(blank=True, null=True)
    الاجزاء_المحفوظة = models.TextField(blank=True, null=True)
    مجاز = models.CharField(
        max_length=10,
        choices=اجازة,
        default="غير مجاز",
    )

    الشيخ_المجيز = models.TextField(blank=True, null=True)
    الرواية = models.TextField(blank=True, null=True)
    روايات_اخرى = models.TextField(blank=True, null=True)
    الشيخ_المجيز = models.TextField(blank=True, null=True)
    علوم_القرآن_و_التفسير = models.CharField(max_length=1000)
    الكتاب = models.CharField(max_length=1000, default=" ")
    الشيخ_الذي_قرأت_عليه = models.CharField(max_length=1000, default=" ")
    العقيدة = models.CharField(max_length=1000, default=" ")
    الكتاب = models.CharField(max_length=1000, default=" ")
    الشيخ_الذي_قرأت_عليه = models.CharField(max_length=1000, default=" ")
    النحو = models.CharField(max_length=10000, default=" ")
    الكتاب = models.CharField(max_length=1000, default=" ")
    الشيخ_الذي_قرأت_عليه = models.CharField(max_length=1000, default=" ")
    ترغب_بالتدريس = models.CharField(
        max_length=10,
        choices=cost,
        default="ببدل",
    )
    الفئة_العمرية = models.CharField(
        max_length=10,
        choices=age,
        default="كبار",
    )
    الاوقات_و_الايام_المناسبة_لك = models.CharField
    رأي_اللجنة_العلمية = models.CharField(max_length=1000, default=" ")
    قرار_الادارة = models.CharField(max_length=1000, default=" ")




