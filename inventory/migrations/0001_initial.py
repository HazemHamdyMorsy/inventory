# Generated by Django 4.2.5 on 2023-09-24 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Side',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place', to='inventory.side')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='Movment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
                ('reciver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.side', verbose_name='recive')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send', to='inventory.side')),
            ],
        ),
    ]
