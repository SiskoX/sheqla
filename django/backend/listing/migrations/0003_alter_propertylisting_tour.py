# Generated by Django 3.2.9 on 2022-08-16 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_alter_propertylisting_tour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertylisting',
            name='tour',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='listing.requesttour'),
        ),
    ]
