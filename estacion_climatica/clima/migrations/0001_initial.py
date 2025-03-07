# Generated by Django 5.1.6 on 2025-02-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosClimaticos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('temperatura', models.FloatField()),
                ('humedad', models.FloatField()),
                ('luz', models.FloatField()),
                ('presion', models.FloatField()),
            ],
        ),
    ]
