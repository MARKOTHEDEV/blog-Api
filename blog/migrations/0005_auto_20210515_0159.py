# Generated by Django 3.2 on 2021-05-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_datecreated'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blogPost2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='extrapics',
            field=models.ImageField(default='blog/%d/', null=True, upload_to=''),
        ),
    ]
