# Generated by Django 4.1.4 on 2022-12-16 22:46

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogpage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='intro',
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(to='blog.blogcategory'),
        ),
    ]
