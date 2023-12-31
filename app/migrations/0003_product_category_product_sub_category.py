# Generated by Django 4.2 on 2023-11-06 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.sub_category'),
        ),
    ]
