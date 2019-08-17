# Generated by Django 2.0.13 on 2019-08-03 17:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20190721_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='upvotes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teammember',
            name='username',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z_-]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z_-]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]