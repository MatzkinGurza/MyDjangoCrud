# Generated by Django 5.1.2 on 2024-11-04 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CrudBlog", "0007_category_post_category_alter_post_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="tag",
            field=models.CharField(max_length=255),
        ),
    ]
