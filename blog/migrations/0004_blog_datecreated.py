# Generated by Django 3.2 on 2021-05-14 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210514_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='dateCreated',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
