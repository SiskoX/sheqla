# Generated by Django 3.2.9 on 2022-10-01 07:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0019_alter_favourite_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertylisting',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
