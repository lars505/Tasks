# Generated by Django 5.0.3 on 2024-04-26 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listado', '0003_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='imagen',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
