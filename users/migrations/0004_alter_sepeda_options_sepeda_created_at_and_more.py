# Generated by Django 5.1.2 on 2024-12-03 05:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_stasiun_sepeda_stasiun'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sepeda',
            options={'ordering': ['status_sepeda', 'tipe_sepeda'], 'verbose_name': 'Sepeda', 'verbose_name_plural': 'Sepeda'},
        ),
        migrations.AddField(
            model_name='sepeda',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sepeda',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='sepeda',
            name='status_sepeda',
            field=models.CharField(choices=[('tersedia', 'Tersedia'), ('dipinjam', 'Dipinjam'), ('pemeliharaan', 'Pemeliharaan')], default='tersedia', max_length=15),
        ),
    ]
