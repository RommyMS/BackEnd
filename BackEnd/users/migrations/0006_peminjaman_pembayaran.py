# Generated by Django 5.1.2 on 2024-12-09 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_stasiun_options_stasiun_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peminjaman',
            fields=[
                ('id_peminjaman', models.AutoField(primary_key=True, serialize=False)),
                ('total_biaya', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('tanggal_peminjaman', models.DateTimeField(auto_now_add=True)),
                ('lama_peminjaman', models.DurationField()),
                ('status_peminjaman', models.CharField(choices=[('aktif', 'Aktif'), ('selesai', 'Selesai'), ('dibatalkan', 'Dibatalkan')], default='aktif', max_length=20)),
                ('id_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='peminjaman', to='users.customer')),
                ('id_sepeda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='peminjaman', to='users.sepeda')),
                ('id_stasiun', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='peminjaman', to='users.stasiun')),
            ],
            options={
                'verbose_name': 'Peminjaman',
                'verbose_name_plural': 'Peminjaman',
                'ordering': ['-tanggal_peminjaman'],
            },
        ),
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('id_pembayaran', models.AutoField(primary_key=True, serialize=False)),
                ('jumlah_pembayaran', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status_pembayaran', models.CharField(choices=[('belum', 'Belum Dibayar'), ('lunas', 'Lunas')], max_length=20)),
                ('metode_pembayaran', models.CharField(max_length=50)),
                ('bukti_pembayaran', models.ImageField(blank=True, null=True, upload_to='bukti_pembayaran/')),
                ('tanggal_pembayaran', models.DateTimeField(auto_now_add=True)),
                ('id_peminjaman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.peminjaman')),
            ],
            options={
                'verbose_name': 'Pembayaran',
                'verbose_name_plural': 'Pembayaran',
            },
        ),
    ]