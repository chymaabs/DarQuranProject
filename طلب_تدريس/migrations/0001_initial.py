# Generated by Django 4.1 on 2022-08-19 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='بيروت',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('الاسم_الثلاثي', models.CharField(default=' ', max_length=200)),
                ('الهاتف', models.IntegerField()),
                ('تاريخ_الميلاد', models.CharField(max_length=100)),
                ('العمل_الحالي', models.TextField(blank=True, null=True)),
                ('مكان_الاقامة', models.TextField(blank=True, null=True)),
                ('المعرف', models.TextField(blank=True, null=True)),
                ('الوضع_العائلي', models.CharField(choices=[('اعزب', 'اعزب'), ('متزوج', 'متزوج'), ('منفصل', 'منفصل')], default='اعزب', max_length=10)),
                ('التاريخ', models.TextField(blank=True, null=True)),
                ('المدرسة_او_الجامعة', models.CharField(max_length=100)),
                ('الصف_او_التخصص', models.CharField(max_length=100)),
                ('شهادات_اخرى', models.TextField(blank=True, null=True)),
                ('الاجزاء_المحفوظة', models.TextField(blank=True, null=True)),
                ('مجاز', models.CharField(choices=[('مجاز', 'مجاز'), ('غير مجاز', 'غير مجاز')], default='غير مجاز', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='صيدا',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('الاسم_الثلاثي', models.CharField(default=' ', max_length=200)),
                ('الهاتف', models.IntegerField()),
                ('تاريخ_الميلاد', models.CharField(max_length=100)),
                ('العمل_الحالي', models.TextField(blank=True, null=True)),
                ('مكان_الاقامة', models.TextField(blank=True, null=True)),
                ('المعرف', models.TextField(blank=True, null=True)),
                ('الوضع_العائلي', models.CharField(choices=[('اعزب', 'اعزب'), ('متزوج', 'متزوج'), ('منفصل', 'منفصل')], default='اعزب', max_length=10)),
                ('التاريخ', models.TextField(blank=True, null=True)),
                ('المدرسة_او_الجامعة', models.CharField(max_length=100)),
                ('الصف_او_التخصص', models.CharField(max_length=100)),
                ('شهادات_اخرى', models.TextField(blank=True, null=True)),
                ('الاجزاء_المحفوظة', models.TextField(blank=True, null=True)),
                ('مجاز', models.CharField(choices=[('مجاز', 'مجاز'), ('غير مجاز', 'غير مجاز')], default='غير مجاز', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='طرابلس',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('الاسم_الثلاثي', models.CharField(default=' ', max_length=200)),
                ('الهاتف', models.IntegerField()),
                ('تاريخ_الميلاد', models.CharField(max_length=100)),
                ('العمل_الحالي', models.TextField(blank=True, null=True)),
                ('مكان_الاقامة', models.TextField(blank=True, null=True)),
                ('المعرف', models.TextField(blank=True, null=True)),
                ('الوضع_العائلي', models.CharField(choices=[('اعزب', 'اعزب'), ('متزوج', 'متزوج'), ('منفصل', 'منفصل')], default='اعزب', max_length=10)),
                ('التاريخ', models.TextField(blank=True, null=True)),
                ('المدرسة_او_الجامعة', models.CharField(max_length=100)),
                ('الصف_او_التخصص', models.CharField(max_length=100)),
                ('شهادات_اخرى', models.TextField(blank=True, null=True)),
                ('الاجزاء_المحفوظة', models.TextField(blank=True, null=True)),
                ('مجاز', models.CharField(choices=[('مجاز', 'مجاز'), ('غير مجاز', 'غير مجاز')], default='غير مجاز', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='عرمون',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('الاسم_الثلاثي', models.CharField(default=' ', max_length=200)),
                ('الهاتف', models.IntegerField()),
                ('تاريخ_الميلاد', models.CharField(max_length=100)),
                ('العمل_الحالي', models.TextField(blank=True, null=True)),
                ('مكان_الاقامة', models.TextField(blank=True, null=True)),
                ('المعرف', models.TextField(blank=True, null=True)),
                ('الوضع_العائلي', models.CharField(choices=[('اعزب', 'اعزب'), ('متزوج', 'متزوج'), ('منفصل', 'منفصل')], default='اعزب', max_length=10)),
                ('التاريخ', models.TextField(blank=True, null=True)),
                ('المدرسة_او_الجامعة', models.CharField(max_length=100)),
                ('الصف_او_التخصص', models.CharField(max_length=100)),
                ('شهادات_اخرى', models.TextField(blank=True, null=True)),
                ('الاجزاء_المحفوظة', models.TextField(blank=True, null=True)),
                ('مجاز', models.CharField(choices=[('مجاز', 'مجاز'), ('غير مجاز', 'غير مجاز')], default='غير مجاز', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='عكار',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('الاسم_الثلاثي', models.CharField(default=' ', max_length=200)),
                ('الهاتف', models.IntegerField()),
                ('تاريخ_الميلاد', models.CharField(max_length=100)),
                ('العمل_الحالي', models.TextField(blank=True, null=True)),
                ('مكان_الاقامة', models.TextField(blank=True, null=True)),
                ('المعرف', models.TextField(blank=True, null=True)),
                ('الوضع_العائلي', models.CharField(choices=[('اعزب', 'اعزب'), ('متزوج', 'متزوج'), ('منفصل', 'منفصل')], default='اعزب', max_length=10)),
                ('التاريخ', models.TextField(blank=True, null=True)),
                ('المدرسة_او_الجامعة', models.CharField(max_length=100)),
                ('الصف_او_التخصص', models.CharField(max_length=100)),
                ('شهادات_اخرى', models.TextField(blank=True, null=True)),
                ('الاجزاء_المحفوظة', models.TextField(blank=True, null=True)),
                ('مجاز', models.CharField(choices=[('مجاز', 'مجاز'), ('غير مجاز', 'غير مجاز')], default='غير مجاز', max_length=10)),
            ],
        ),
    ]
