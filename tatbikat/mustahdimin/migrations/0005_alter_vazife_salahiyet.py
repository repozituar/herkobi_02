# Generated by Django 4.1 on 2022-10-23 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mustahdimin', '0004_mesuliyet_salahiyet_muvazzaf_vazife_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vazife',
            name='salahiyet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mustahdimin.salahiyet'),
        ),
    ]