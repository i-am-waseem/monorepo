# Generated by Django 4.1.5 on 2023-08-30 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datahub", "0053_alter_organization_org_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="usagepolicy",
            name="configs",
            field=models.JSONField(default=dict, null=True),
        ),
    ]
