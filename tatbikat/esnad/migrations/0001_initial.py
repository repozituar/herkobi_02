# Generated by Django 4.1 on 2022-10-23 09:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mustecirin', '0001_initial'),
        ('mesanid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sened',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('kayit_tarihi', models.DateTimeField(auto_now_add=True)),
                ('tadilat_tarihi', models.DateTimeField(auto_now=True)),
                ('hesabini_muktariz', models.BooleanField(default=True)),
                ('mustened', models.BooleanField(default=False)),
                ('izafe_edildi', models.BooleanField(default=False)),
                ('belge_no', models.CharField(blank=True, max_length=36, null=True)),
                ('belge_tarihi', models.DateTimeField(auto_now_add=True)),
                ('hesab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hesab', to='mesanid.hesab')),
                ('mahsub', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mahsub', to='mesanid.hesab')),
                ('mustecir', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mustecirin.mustecir')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mazmun',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('kayit_tarihi', models.DateTimeField(auto_now_add=True)),
                ('tadilat_tarihi', models.DateTimeField(auto_now=True)),
                ('mustened', models.BooleanField(default=False)),
                ('izafe_edildi', models.BooleanField(default=False)),
                ('meblag', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'En fazla 9999999.99.'}}, help_text='MEn fazla 9999999.99', max_digits=9, verbose_name='Meblağ')),
                ('hesab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mazmun_hesabi', to='mesanid.hesab')),
                ('mahsub', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mazmun_mahsubu', to='mesanid.hesab')),
                ('mustecir', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mustecirin.mustecir')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Kalem',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('kayit_tarihi', models.DateTimeField(auto_now_add=True)),
                ('tadilat_tarihi', models.DateTimeField(auto_now=True)),
                ('mustened', models.BooleanField(default=False)),
                ('izafe_edildi', models.BooleanField(default=False)),
                ('aded', models.IntegerField()),
                ('birim', models.CharField(blank=True, max_length=124, null=True)),
                ('fiyat', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'En fazla 99999.99.'}}, help_text='MEn fazla 99999.99', max_digits=7, verbose_name='Fiyat')),
                ('hesab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kalem_hesabi', to='mesanid.hesab')),
                ('mahsub', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kalem_mahsubu', to='mesanid.hesab')),
                ('mustecir', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mustecirin.mustecir')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]