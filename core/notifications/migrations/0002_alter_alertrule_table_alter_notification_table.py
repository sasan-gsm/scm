# Generated by Django 4.2.9 on 2025-03-25 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="alertrule",
            table="alert_rules",
        ),
        migrations.AlterModelTable(
            name="notification",
            table="notifications",
        ),
    ]
