# Generated by Django 3.2 on 2021-05-14 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210515_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='contentHeader',
            field=models.ImageField(null=True, upload_to='blog/%d/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='extrapics',
            field=models.ImageField(null=True, upload_to='blog/%d/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='introPics',
            field=models.ImageField(null=True, upload_to='blog/%d/'),
        ),
    ]
