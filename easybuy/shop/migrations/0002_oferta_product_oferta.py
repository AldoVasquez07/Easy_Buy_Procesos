# Generated by Django 5.1.2 on 2024-10-10 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('descripcion', models.TextField(blank=True)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'ordering': ['motivo'],
                'indexes': [models.Index(fields=['id', 'slug'], name='shop_oferta_id_294eeb_idx'), models.Index(fields=['motivo'], name='shop_oferta_motivo_a6f656_idx')],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='oferta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.oferta'),
        ),
    ]
