# Generated by Django 4.0.5 on 2022-09-28 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datahub', '0001_initial'),
        ('participant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datahub.organization'),
        ),
    ]
