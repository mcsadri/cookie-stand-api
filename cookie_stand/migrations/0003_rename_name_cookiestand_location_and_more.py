# Generated by Django 4.1.5 on 2023-08-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cookie_stand", "0002_rename_thing_cookiestand"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cookiestand",
            old_name="name",
            new_name="location",
        ),
        migrations.RenameField(
            model_name="cookiestand",
            old_name="reviewer",
            new_name="owner",
        ),
        migrations.RemoveField(
            model_name="cookiestand",
            name="rating",
        ),
        migrations.AddField(
            model_name="cookiestand",
            name="average_cookies_per_sale",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="cookiestand",
            name="hourly_sales",
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AddField(
            model_name="cookiestand",
            name="maximum_customers_per_hour",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="cookiestand",
            name="minimum_customers_per_hour",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="cookiestand",
            name="description",
            field=models.TextField(blank=True, default=True),
            preserve_default=False,
        ),
    ]
