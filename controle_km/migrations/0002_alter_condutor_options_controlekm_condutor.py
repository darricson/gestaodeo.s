# Generated by Django 4.0.4 on 2022-06-12 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle_km', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='condutor',
            options={'verbose_name': 'CONDUTOR', 'verbose_name_plural': 'CONDUTORES'},
        ),
        migrations.AddField(
            model_name='controlekm',
            name='condutor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='controle_km.condutor', verbose_name='MOTORISTA'),
            preserve_default=False,
        ),
    ]