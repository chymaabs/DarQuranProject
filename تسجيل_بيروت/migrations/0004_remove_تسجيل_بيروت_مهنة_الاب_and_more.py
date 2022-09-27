# Generated by Django 4.1 on 2022-08-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('تسجيل_بيروت', '0003_remove_تسجيل_بيروت_الاسم_الثلاثي'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='تسجيل_بيروت',
            name='مهنة_الاب',
        ),
        migrations.RemoveField(
            model_name='تسجيل_بيروت',
            name='مهنة_الام',
        ),
        migrations.RemoveField(
            model_name='تسجيل_بيروت',
            name='هاتف_الام',
        ),
        migrations.AddField(
            model_name='تسجيل_بيروت',
            name='الاسم_الثلاثي',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='تسجيل_بيروت',
            name='المستوى_الذي_تود_القراءة_فيه',
            field=models.CharField(choices=[('تلاوة', 'تلاوة'), ('قراءات', 'قراءات'), ('حفظ', 'حفظ')], default='حفظ', max_length=10),
        ),
        migrations.AddField(
            model_name='تسجيل_بيروت',
            name='الوضع_العائلي',
            field=models.CharField(choices=[('اعزب', 'اعزب'), ('متزوج', 'متزوج'), ('منفصل', 'منفصل')], default='اعزب', max_length=10),
        ),
    ]
