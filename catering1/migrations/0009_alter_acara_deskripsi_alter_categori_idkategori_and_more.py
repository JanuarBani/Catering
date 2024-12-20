# Generated by Django 5.1.1 on 2024-10-29 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catering1', '0008_alter_cateringmenu_idkate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acara',
            name='deskripsi',
            field=models.TextField(verbose_name='Deskripsi'),
        ),
        migrations.AlterField(
            model_name='categori',
            name='idKategori',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID Kategori'),
        ),
        migrations.AlterField(
            model_name='categorimenu',
            name='idKate',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='idKate'),
        ),
        migrations.AlterField(
            model_name='cateringmenu',
            name='deskripsi',
            field=models.TextField(verbose_name='Deskripsi'),
        ),
        migrations.AlterField(
            model_name='cateringmenu',
            name='idMenu',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID Menu'),
        ),
        migrations.AlterField(
            model_name='notelepon',
            name='idNoTelp',
            field=models.TextField(primary_key=True, serialize=False, verbose_name='ID Telepon'),
        ),
        migrations.AlterField(
            model_name='pelanggan',
            name='alamat',
            field=models.TextField(verbose_name='Alamat'),
        ),
        migrations.AlterField(
            model_name='pelanggan',
            name='idPelanggan',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID Pelanggan'),
        ),
        migrations.AlterField(
            model_name='pemesananacara',
            name='status',
            field=models.CharField(choices=[('tertunda', 'Tertunda'), ('konfirmasi', 'Dikonfirmasi'), ('dibatalkan', 'Dibatalkan'), ('dikirim', 'Dikirim'), ('diterima', 'Diterima')], default='pending', max_length=20, verbose_name='Status Pesanan'),
        ),
        migrations.AlterField(
            model_name='pemesananpelanggan',
            name='status',
            field=models.CharField(choices=[('tertunda', 'Tertunda'), ('konfirmasi', 'Dikonfirmasi'), ('dibatalkan', 'Dibatalkan'), ('dikirim', 'Dikirim'), ('diterima', 'Diterima')], default='pending', max_length=20, verbose_name='Status Pesanan'),
        ),
    ]
