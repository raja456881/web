# Generated by Django 3.1 on 2020-09-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200902_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]