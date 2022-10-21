# Generated by Django 4.1 on 2022-10-21 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mustecirin', '0001_initial'),
        ('mustahdimin', '0002_tarihce'),
    ]

    operations = [
        migrations.AddField(
            model_name='mustahdim',
            name='ad',
            field=models.CharField(blank=True, max_length=124, null=True),
        ),
        migrations.AddField(
            model_name='mustahdim',
            name='mumtaz',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mustahdim',
            name='mustecir',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mustecirin.mustecir'),
        ),
        migrations.AddField(
            model_name='mustahdim',
            name='soyad',
            field=models.CharField(blank=True, max_length=124, null=True),
        ),
    ]
