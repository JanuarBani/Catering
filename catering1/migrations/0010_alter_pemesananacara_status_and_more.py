# Generated by Django 5.1.1 on 2024-10-29 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catering1', '0009_alter_acara_deskripsi_alter_categori_idkategori_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pemesananacara',
            name='status',
            field=models.CharField(choices=[('tertunda', 'Tertunda'), ('konfirmasi', 'Dikonfirmasi'), ('dibatalkan', 'Dibatalkan'), ('dikirim', 'Dikirim'), ('diterima', 'Diterima')], max_length=20, verbose_name='Status Pesanan'),
        ),
        migrations.AlterField(
            model_name='pemesananpelanggan',
            name='status',
            field=models.CharField(choices=[('tertunda', 'Tertunda'), ('konfirmasi', 'Dikonfirmasi'), ('dibatalkan', 'Dibatalkan'), ('dikirim', 'Dikirim'), ('diterima', 'Diterima')], max_length=20, verbose_name='Status Pesanan'),
        ),
    ]
