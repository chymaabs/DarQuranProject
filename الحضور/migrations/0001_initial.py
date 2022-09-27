# Generated by Django 4.1 on 2022-08-18 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('تسجيل_بيروت', '0006_تسجيل_صيدا_التاريخ_تسجيل_طرابلس_التاريخ_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='الحضور',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RollNo', models.CharField(blank=True, max_length=46, null=True)),
                ('student_name', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('absent', 'Absent'), ('present', 'Present')], max_length=8)),
                ('الاسم_الثلاثي', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='تسجيل_بيروت.تسجيل_بيروت')),
            ],
        ),
    ]
