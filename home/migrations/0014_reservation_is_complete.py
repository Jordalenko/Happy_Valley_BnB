# Generated by Django 4.2.20 on 2025-05-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_complete_res_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
