# Generated by Django 5.1.3 on 2024-11-25 23:40

import apps.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Crop',
                'verbose_name_plural': 'Crops',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('cpf_cnpj', models.CharField(validators=[apps.common.validators.CpfCnpjValidator()])),
                ('name', models.CharField(max_length=255)),
                ('farm_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=2)),
                ('total_area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cultivable_area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vegetation_area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('planted_crops', models.ManyToManyField(blank=True, related_name='producers', to='producer.crop')),
            ],
            options={
                'verbose_name': 'producer',
                'verbose_name_plural': 'producers',
                'db_table': 'producers',
                'ordering': ['created_at'],
            },
        ),
    ]
