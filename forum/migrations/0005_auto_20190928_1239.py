# Generated by Django 2.0.13 on 2019-09-28 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20190928_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='upvotes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
