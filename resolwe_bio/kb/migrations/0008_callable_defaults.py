# Generated by Django 2.2 on 2019-04-29 13:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resolwe_bio_kb', '0007_feature_fullname_350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='aliases',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), blank=True, default=list, size=None),
        ),
    ]