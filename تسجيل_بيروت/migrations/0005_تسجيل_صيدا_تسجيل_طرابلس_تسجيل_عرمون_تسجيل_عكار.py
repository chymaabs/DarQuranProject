# Generated by Django 4.1 on 2022-08-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('تسجيل_بيروت', '0004_remove_تسجيل_بيروت_مهنة_الاب_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='تسجيل_صيدا',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('الاسم_الثلاثي', models.CharField(default=' ', max_length=200)),
                ('الهاتف', models.IntegerField()),
                ('تاريخ_الميلاد', models.CharField(max_length=100)),
                ('العمر', models.IntegerField()),
                ('اسم_الام', models.CharField(max_length=100)),
                ('الجنسية', models.CharField(max_length=100)),
                ('المدرسة_او_الجامعة', models.CharField(max_length=100)),
                ('الصف_او_التخصص', models.CharField(max_length=100)),
                ('التقدير', models.CharField(max_length=100)),
                ('محفوظاته_من_القران', models.CharField(default='0', max_length=300)),
                ('مستوى_القراءة_بالقران', models.CharField(choices=[('مبتدئ', 'مبتدئ'), ('قارئ', 'قارئ'), ('حافظ', 'حافظ'), ('مجاز', 'مجاز')], default='مبتدئ', max_length=10)),
                ('المستوى_الذي_تود_القراءة_فيه', models.CharField(choices=[('تلاوة', 'تلاوة'), ('قراءات', 'قراءات'), ('حفظ', 'حفظ')], default='حفظ', max_length=10)),
                ('الوضع_العائلي', models.CharField(choices=[('اعزب', 'اعزب'), ('متزوج', 'متزوج'), ('منفصل', 'منفصل')], default='اعزب', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='تسجيل_طرابلس',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('الاسم_الثلاثي', models.CharField(default=' ', max_length=200)),
                ('الهاتف', models.IntegerField()),
                ('تاريخ_الميلاد', models.CharField(max_length=100)),
                ('العمر', models.IntegerField()),
                ('اسم_الام', models.CharField(max_length=100)),
                ('الجنسية', models.CharField(max_length=100)),
                ('المدرسة_او_الجامعة', models.CharField(max_length=100)),
                ('الصف_او_التخصص', models.CharField(max_length=100)),
                ('التقدير', models.CharField(max_length=100)),
                ('محفوظاته_من_القران', models.CharField(default='0', max_length=300)),
                ('مستوى_القراءة_بالقران', models.CharField(choices=[('مبتدئ', 'مبتدئ'), ('قارئ', 'قارئ'), ('حافظ', 'حافظ'), ('مجاز', 'مجاز')], default='مبتدئ', max_length=10)),
                ('المستوى_الذي_تود_القراءة_فيه', models.CharField(choices=[('تلاوة', 'تلاوة'), ('قراءات', 'قراءات'), ('حفظ', 'حفظ')], default='حفظ', max_length=10)),
                ('الوضع_العائلي', models.CharField(choices=[('اعزب', 'اعزب'), ('متزوج', 'متزوج'), ('منفصل', 'منفصل')], default='اعزب', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='تسجيل_عرمون',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('الاسم_الثلاثي', models.CharField(default=' ', max_length=200)),
                ('الهاتف', models.IntegerField()),
                ('تاريخ_الميلاد', models.CharField(max_length=100)),
                ('العمر', models.IntegerField()),
                ('اسم_الام', models.CharField(max_length=100)),
                ('الجنسية', models.CharField(max_length=100)),
                ('المدرسة_او_الجامعة', models.CharField(max_length=100)),
                ('الصف_او_التخصص', models.CharField(max_length=100)),
                ('التقدير', models.CharField(max_length=100)),
                ('محفوظاته_من_القران', models.CharField(default='0', max_length=300)),
                ('مستوى_القراءة_بالقران', models.CharField(choices=[('مبتدئ', 'مبتدئ'), ('قارئ', 'قارئ'), ('حافظ', 'حافظ'), ('مجاز', 'مجاز')], default='مبتدئ', max_length=10)),
                ('المستوى_الذي_تود_القراءة_فيه', models.CharField(choices=[('تلاوة', 'تلاوة'), ('قراءات', 'قراءات'), ('حفظ', 'حفظ')], default='حفظ', max_length=10)),
                ('الوضع_العائلي', models.CharField(choices=[('اعزب', 'اعزب'), ('متزوج', 'متزوج'), ('منفصل', 'منفصل')], default='اعزب', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='تسجيل_عكار',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('الاسم_الثلاثي', models.CharField(default=' ', max_length=200)),
                ('الهاتف', models.IntegerField()),
                ('تاريخ_الميلاد', models.CharField(max_length=100)),
                ('العمر', models.IntegerField()),
                ('اسم_الام', models.CharField(max_length=100)),
                ('الجنسية', models.CharField(max_length=100)),
                ('المدرسة_او_الجامعة', models.CharField(max_length=100)),
                ('الصف_او_التخصص', models.CharField(max_length=100)),
                ('التقدير', models.CharField(max_length=100)),
                ('محفوظاته_من_القران', models.CharField(default='0', max_length=300)),
                ('مستوى_القراءة_بالقران', models.CharField(choices=[('مبتدئ', 'مبتدئ'), ('قارئ', 'قارئ'), ('حافظ', 'حافظ'), ('مجاز', 'مجاز')], default='مبتدئ', max_length=10)),
                ('المستوى_الذي_تود_القراءة_فيه', models.CharField(choices=[('تلاوة', 'تلاوة'), ('قراءات', 'قراءات'), ('حفظ', 'حفظ')], default='حفظ', max_length=10)),
                ('الوضع_العائلي', models.CharField(choices=[('اعزب', 'اعزب'), ('متزوج', 'متزوج'), ('منفصل', 'منفصل')], default='اعزب', max_length=10)),
            ],
        ),
    ]
