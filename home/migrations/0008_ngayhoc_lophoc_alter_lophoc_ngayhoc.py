# Generated by Django 4.0.5 on 2022-06-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_ngayhoc_lophoc_alter_lophoc_ngayhoc'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngayhoc',
            name='lopHoc',
            field=models.ManyToManyField(to='home.lophoc'),
        ),
        migrations.AlterField(
            model_name='lophoc',
            name='ngayHoc',
            field=models.ManyToManyField(blank=True, null=True, to='home.ngayhoc'),
        ),
    ]
