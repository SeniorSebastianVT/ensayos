# Generated by Django 5.0.6 on 2024-07-11 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aprendiz',
            fields=[
                ('id_aprendiz', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=40, verbose_name='Nombres')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha Nacimiento')),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, verbose_name='Telefono')),
            ],
            options={
                'db_table': 'aprendiz',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Calificaciones',
            fields=[
                ('id_calificacion', models.AutoField(primary_key=True, serialize=False)),
                ('id_aprendiz', models.IntegerField()),
                ('id_curso', models.IntegerField()),
                ('nota', models.IntegerField()),
            ],
            options={
                'db_table': 'calificaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False)),
                ('id_aprendiz', models.IntegerField()),
                ('curso', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'cursos',
                'managed': False,
            },
        ),
    ]
