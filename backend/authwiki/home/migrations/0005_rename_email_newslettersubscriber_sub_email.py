# Generated by Django 4.1.4 on 2022-12-14 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_newslettersubscriber_delete_subscribedusers"),
    ]

    operations = [
        migrations.RenameField(
            model_name="newslettersubscriber", old_name="email", new_name="sub_email",
        ),
    ]