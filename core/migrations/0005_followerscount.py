# Generated by Django 4.1 on 2022-09-22 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_rename_post_is_likepost_post_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="FollowersCount",
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
                ("follower", models.CharField(max_length=100)),
                ("user", models.CharField(max_length=100)),
            ],
        ),
    ]
