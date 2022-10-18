# Generated by Django 3.2.9 on 2022-08-20 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.IntegerField()),
                ('full_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('bank', models.CharField(choices=[('cbe', 'CBE'), ('abyssinia', 'Abyssinia'), ('awash', 'Awash')], max_length=30)),
                ('receipt', models.ImageField(blank=True, null=True, upload_to='recept/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.BooleanField(default=False)),
                ('bank_transfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.banktransfer')),
            ],
        ),
    ]
