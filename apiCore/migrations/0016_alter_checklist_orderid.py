# Generated by Django 3.2.9 on 2021-12-12 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiCore', '0015_rename_iduser_order_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='orderID',
            field=models.IntegerField(),
        ),
    ]