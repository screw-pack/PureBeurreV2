# Generated by Django 3.1.7 on 2021-03-19 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('substitute', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ingredients',
            field=models.TextField(blank=True, null=True),
        ),
    ]
