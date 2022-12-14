# Generated by Django 4.1 on 2022-08-19 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('طلب_تدريس', '0002_صيدا_الرواية_صيدا_الشيخ_المجيز_صيدا_رواي_اتاخرى_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='صيدا',
            old_name='رواي_اتاخرى',
            new_name='روايات_اخرى',
        ),
        migrations.RenameField(
            model_name='طرابلس',
            old_name='رواي_اتاخرى',
            new_name='روايات_اخرى',
        ),
        migrations.RenameField(
            model_name='عرمون',
            old_name='رواي_اتاخرى',
            new_name='روايات_اخرى',
        ),
        migrations.RenameField(
            model_name='عكار',
            old_name='رواي_اتاخرى',
            new_name='روايات_اخرى',
        ),
        migrations.AddField(
            model_name='بيروت',
            name='الرواية',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='بيروت',
            name='الشيخ_الذي_قرأت_عليه',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='بيروت',
            name='الشيخ_المجيز',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='بيروت',
            name='العقيدة',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='بيروت',
            name='الفئة_العمرية',
            field=models.CharField(choices=[('كبار', 'كبار'), ('صغار', 'صغار')], default='كبار', max_length=10),
        ),
        migrations.AddField(
            model_name='بيروت',
            name='الكتاب',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='بيروت',
            name='النحو',
            field=models.CharField(default=' ', max_length=10000),
        ),
        migrations.AddField(
            model_name='بيروت',
            name='ترغب_بالتدريس',
            field=models.CharField(choices=[('ببدل', 'ببدل'), ('كبار', 'كبار')], default='ببدل', max_length=10),
        ),
        migrations.AddField(
            model_name='بيروت',
            name='رأي_اللجنة_العلمية',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='بيروت',
            name='روايات_اخرى',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='بيروت',
            name='علوم_القرآن_و_التفسير',
            field=models.CharField(default=' ', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='بيروت',
            name='قرار_الادارة',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='صيدا',
            name='الشيخ_الذي_قرأت_عليه',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='صيدا',
            name='العقيدة',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='صيدا',
            name='الفئة_العمرية',
            field=models.CharField(choices=[('كبار', 'كبار'), ('صغار', 'صغار')], default='كبار', max_length=10),
        ),
        migrations.AddField(
            model_name='صيدا',
            name='الكتاب',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='صيدا',
            name='النحو',
            field=models.CharField(default=' ', max_length=10000),
        ),
        migrations.AddField(
            model_name='صيدا',
            name='ترغب_بالتدريس',
            field=models.CharField(choices=[('ببدل', 'ببدل'), ('كبار', 'كبار')], default='ببدل', max_length=10),
        ),
        migrations.AddField(
            model_name='صيدا',
            name='رأي_اللجنة_العلمية',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='صيدا',
            name='علوم_القرآن_و_التفسير',
            field=models.CharField(default=' ', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='صيدا',
            name='قرار_الادارة',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='طرابلس',
            name='الشيخ_الذي_قرأت_عليه',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='طرابلس',
            name='العقيدة',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='طرابلس',
            name='الفئة_العمرية',
            field=models.CharField(choices=[('كبار', 'كبار'), ('صغار', 'صغار')], default='كبار', max_length=10),
        ),
        migrations.AddField(
            model_name='طرابلس',
            name='الكتاب',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='طرابلس',
            name='النحو',
            field=models.CharField(default=' ', max_length=10000),
        ),
        migrations.AddField(
            model_name='طرابلس',
            name='ترغب_بالتدريس',
            field=models.CharField(choices=[('ببدل', 'ببدل'), ('كبار', 'كبار')], default='ببدل', max_length=10),
        ),
        migrations.AddField(
            model_name='طرابلس',
            name='رأي_اللجنة_العلمية',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='طرابلس',
            name='علوم_القرآن_و_التفسير',
            field=models.CharField(default=' ', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='طرابلس',
            name='قرار_الادارة',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='عرمون',
            name='الشيخ_الذي_قرأت_عليه',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='عرمون',
            name='العقيدة',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='عرمون',
            name='الفئة_العمرية',
            field=models.CharField(choices=[('كبار', 'كبار'), ('صغار', 'صغار')], default='كبار', max_length=10),
        ),
        migrations.AddField(
            model_name='عرمون',
            name='الكتاب',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='عرمون',
            name='النحو',
            field=models.CharField(default=' ', max_length=10000),
        ),
        migrations.AddField(
            model_name='عرمون',
            name='ترغب_بالتدريس',
            field=models.CharField(choices=[('ببدل', 'ببدل'), ('كبار', 'كبار')], default='ببدل', max_length=10),
        ),
        migrations.AddField(
            model_name='عرمون',
            name='رأي_اللجنة_العلمية',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='عرمون',
            name='علوم_القرآن_و_التفسير',
            field=models.CharField(default=' ', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='عرمون',
            name='قرار_الادارة',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='عكار',
            name='الشيخ_الذي_قرأت_عليه',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='عكار',
            name='العقيدة',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='عكار',
            name='الفئة_العمرية',
            field=models.CharField(choices=[('كبار', 'كبار'), ('صغار', 'صغار')], default='كبار', max_length=10),
        ),
        migrations.AddField(
            model_name='عكار',
            name='الكتاب',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='عكار',
            name='النحو',
            field=models.CharField(default=' ', max_length=10000),
        ),
        migrations.AddField(
            model_name='عكار',
            name='ترغب_بالتدريس',
            field=models.CharField(choices=[('ببدل', 'ببدل'), ('كبار', 'كبار')], default='ببدل', max_length=10),
        ),
        migrations.AddField(
            model_name='عكار',
            name='رأي_اللجنة_العلمية',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='عكار',
            name='علوم_القرآن_و_التفسير',
            field=models.CharField(default=' ', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='عكار',
            name='قرار_الادارة',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='بيروت',
            name='الصف_او_التخصص',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='بيروت',
            name='المدرسة_او_الجامعة',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='بيروت',
            name='تاريخ_الميلاد',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='صيدا',
            name='الصف_او_التخصص',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='صيدا',
            name='المدرسة_او_الجامعة',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='صيدا',
            name='تاريخ_الميلاد',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='طرابلس',
            name='الصف_او_التخصص',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='طرابلس',
            name='المدرسة_او_الجامعة',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='طرابلس',
            name='تاريخ_الميلاد',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='عرمون',
            name='الصف_او_التخصص',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='عرمون',
            name='المدرسة_او_الجامعة',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='عرمون',
            name='تاريخ_الميلاد',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='عكار',
            name='الصف_او_التخصص',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='عكار',
            name='المدرسة_او_الجامعة',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='عكار',
            name='تاريخ_الميلاد',
            field=models.CharField(default=' ', max_length=1000),
        ),
    ]
