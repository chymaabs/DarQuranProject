from django.db import models


attendance_choices = (
    ('حاضر', 'حاضر'),
    ('غائب', 'غائب')
)


class بيروت(models.Model):
    الاسم= models.TextField(blank=True, null=True)
    الحضور= models.CharField(max_length=8, choices=attendance_choices, blank=True)
    مكان_الحفظ=models.TextField(blank=True, null=True)
    مكان_المراجعة=models.TextField(blank=True, null=True)
    ملاحظات=models.TextField(blank=True, null=True)


class طرابلس(models.Model):
    الاسم= models.TextField(blank=True, null=True)
    الحضور= models.CharField(max_length=8, choices=attendance_choices, blank=True)
    مكان_الحفظ=models.TextField(blank=True, null=True)
    مكان_المراجعة=models.TextField(blank=True, null=True)
    ملاحظات=models.TextField(blank=True, null=True)


class عكار(models.Model):
    الاسم= models.TextField(blank=True, null=True)
    الحضور= models.CharField(max_length=8, choices=attendance_choices, blank=True)
    مكان_الحفظ=models.TextField(blank=True, null=True)
    مكان_المراجعة=models.TextField(blank=True, null=True)
    ملاحظات=models.TextField(blank=True, null=True)

class عرمون(models.Model):
    الاسم= models.TextField(blank=True, null=True)
    الحضور= models.CharField(max_length=8, choices=attendance_choices, blank=True)
    مكان_الحفظ=models.TextField(blank=True, null=True)
    مكان_المراجعة=models.TextField(blank=True, null=True)
    ملاحظات=models.TextField(blank=True, null=True)

class صيدا(models.Model):
    الاسم= models.TextField(blank=True, null=True)
    الحضور= models.CharField(max_length=8, choices=attendance_choices, blank=True)
    مكان_الحفظ=models.TextField(blank=True, null=True)
    مكان_المراجعة=models.TextField(blank=True, null=True)
    ملاحظات=models.TextField(blank=True, null=True)