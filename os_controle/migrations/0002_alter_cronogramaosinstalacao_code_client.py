# Generated by Django 4.0.4 on 2022-05-29 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('os_controle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronogramaosinstalacao',
            name='code_client',
            field=models.CharField(max_length=40, verbose_name='COD - Cliente'),
        ),
    ]
