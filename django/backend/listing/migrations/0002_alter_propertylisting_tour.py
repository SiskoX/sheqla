# Generated by Django 3.2.9 on 2022-08-16 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertylisting',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.requesttour'),
        ),
    ]
