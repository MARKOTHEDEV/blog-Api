# Generated by Django 3.2 on 2021-05-13 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210513_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='contentHeader',
            field=models.ImageField(default='blog/%d/', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='introPics',
            field=models.ImageField(default='blog/%d/', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
