# Generated by Django 5.1.2 on 2024-11-03 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CrudBlog", "0006_post_image_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="Unspecified", max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.CharField(default="Unspecified", max_length=255),
        ),
        migrations.AlterField(
            model_name="post",
            name="tag",
            field=models.CharField(default="Unspecified", max_length=255),
        ),
    ]
