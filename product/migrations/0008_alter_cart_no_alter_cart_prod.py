# Generated by Django 4.0.3 on 2022-05-19 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_cart_no_alter_cart_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='no',
            field=models.DecimalField(decimal_places=0, max_digits=11),
        ),
        migrations.AlterField(
            model_name='cart',
            name='prod',
            field=models.DecimalField(decimal_places=0, max_digits=11),
        ),
    ]
