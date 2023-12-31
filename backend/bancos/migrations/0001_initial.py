# Generated by Django 4.2.5 on 2023-09-24 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bancos.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='CuentaBancaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_cuenta', models.CharField(max_length=20, unique=True)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bloqueada', models.BooleanField(default=False)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bancos.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.CharField(max_length=20)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bancos.cuentabancaria')),
            ],
        ),
    ]
