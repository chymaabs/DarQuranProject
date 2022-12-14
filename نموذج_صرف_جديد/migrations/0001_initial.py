# Generated by Django 4.1 on 2022-08-20 20:10

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
                ('لامر', models.CharField(default=' ', max_length=1000)),
                ('مبلغ_قدره', models.CharField(default=' ', max_length=1000)),
                ('نقد_او_شيك', models.CharField(default=' ', max_length=1000)),
                ('رقم_الشيك', models.CharField(default=' ', max_length=1000)),
                ('جهةالبنك', models.CharField(default=' ', max_length=1000)),
                ('الموضوع', models.TextField(blank=True, null=True)),
                ('اسم_الحساب', models.CharField(default=' ', max_length=1000)),
                ('المبلغ', models.CharField(default=' ', max_length=1000)),
                ('التاريخ', models.CharField(default=' ', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='صيدا',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('لامر', models.CharField(default=' ', max_length=1000)),
                ('مبلغ_قدره', models.CharField(default=' ', max_length=1000)),
                ('نقد_او_شيك', models.CharField(default=' ', max_length=1000)),
                ('رقم_الشيك', models.CharField(default=' ', max_length=1000)),
                ('جهةالبنك', models.CharField(default=' ', max_length=1000)),
                ('الموضوع', models.TextField(blank=True, null=True)),
                ('اسم_الحساب', models.CharField(default=' ', max_length=1000)),
                ('المبلغ', models.CharField(default=' ', max_length=1000)),
                ('التاريخ', models.CharField(default=' ', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='طرابلس',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('لامر', models.CharField(default=' ', max_length=1000)),
                ('مبلغ_قدره', models.CharField(default=' ', max_length=1000)),
                ('نقد_او_شيك', models.CharField(default=' ', max_length=1000)),
                ('رقم_الشيك', models.CharField(default=' ', max_length=1000)),
                ('جهةالبنك', models.CharField(default=' ', max_length=1000)),
                ('الموضوع', models.TextField(blank=True, null=True)),
                ('اسم_الحساب', models.CharField(default=' ', max_length=1000)),
                ('المبلغ', models.CharField(default=' ', max_length=1000)),
                ('التاريخ', models.CharField(default=' ', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='عرمون',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('لامر', models.CharField(default=' ', max_length=1000)),
                ('مبلغ_قدره', models.CharField(default=' ', max_length=1000)),
                ('نقد_او_شيك', models.CharField(default=' ', max_length=1000)),
                ('رقم_الشيك', models.CharField(default=' ', max_length=1000)),
                ('جهةالبنك', models.CharField(default=' ', max_length=1000)),
                ('الموضوع', models.TextField(blank=True, null=True)),
                ('اسم_الحساب', models.CharField(default=' ', max_length=1000)),
                ('المبلغ', models.CharField(default=' ', max_length=1000)),
                ('التاريخ', models.CharField(default=' ', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='عكار',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('لامر', models.CharField(default=' ', max_length=1000)),
                ('مبلغ_قدره', models.CharField(default=' ', max_length=1000)),
                ('نقد_او_شيك', models.CharField(default=' ', max_length=1000)),
                ('رقم_الشيك', models.CharField(default=' ', max_length=1000)),
                ('جهةالبنك', models.CharField(default=' ', max_length=1000)),
                ('الموضوع', models.TextField(blank=True, null=True)),
                ('اسم_الحساب', models.CharField(default=' ', max_length=1000)),
                ('المبلغ', models.CharField(default=' ', max_length=1000)),
                ('التاريخ', models.CharField(default=' ', max_length=1000)),
            ],
        ),
    ]
