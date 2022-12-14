# Generated by Django 4.1 on 2022-10-22 08:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mustecirin', '0001_initial'),
        ('mesanid', '0001_initial'),
        ('mustahdimin', '0003_mustahdim_ad_mustahdim_mumtaz_mustahdim_mustecir_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesuliyet',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('kayit_tarihi', models.DateTimeField(auto_now_add=True)),
                ('tadilat_tarihi', models.DateTimeField(auto_now=True)),
                ('yol', models.CharField(blank=True, max_length=255, null=True)),
                ('isim', models.CharField(blank=True, max_length=255, null=True, verbose_name='İsim')),
                ('fihrist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mesanid.fihrist')),
                ('mustecir', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mustecirin.mustecir')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Salahiyet',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('kayit_tarihi', models.DateTimeField(auto_now_add=True)),
                ('tadilat_tarihi', models.DateTimeField(auto_now=True)),
                ('yol', models.CharField(blank=True, max_length=255, null=True)),
                ('isim', models.CharField(blank=True, max_length=255, null=True, verbose_name='İsim')),
                ('fihrist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mesanid.fihrist')),
                ('mesuliyet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mustahdimin.mesuliyet')),
                ('mustecir', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mustecirin.mustecir')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Muvazzaf',
            fields=[
            ],
            options={
                'ordering': ('isim',),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('mesanid.hesab',),
        ),
        migrations.CreateModel(
            name='Vazife',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('kayit_tarihi', models.DateTimeField(auto_now_add=True)),
                ('tadilat_tarihi', models.DateTimeField(auto_now=True)),
                ('yol', models.CharField(blank=True, max_length=255, null=True)),
                ('isim', models.CharField(blank=True, max_length=255, null=True, verbose_name='İsim')),
                ('fihrist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mesanid.fihrist')),
                ('mustecir', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mustecirin.mustecir')),
                ('salahiyet', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mustahdimin.salahiyet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='mustahdim',
            name='mesuliyetler',
            field=models.ManyToManyField(blank=True, to='mustahdimin.mesuliyet'),
        ),
        migrations.AddField(
            model_name='mustahdim',
            name='muvazzaf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mustahdimin.muvazzaf'),
        ),
    ]
