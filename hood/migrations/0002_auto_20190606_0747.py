# Generated by Django 2.0 on 2019-06-06 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
