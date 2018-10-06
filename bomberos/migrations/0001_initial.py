# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-10-06 16:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('localidades', '0001_initial'),
        ('personas', '0001_initial'),
        ('grados', '__first__'),
        ('actas', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActaAscenso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_efectiva', models.DateField(verbose_name='Fecha efectiva de Ascenso')),
                ('acta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acta_ascenso', to='actas.Acta', verbose_name='Acta')),
            ],
            options={
                'verbose_name': 'Ascenso',
                'verbose_name_plural': 'Ascensos',
            },
        ),
        migrations.CreateModel(
            name='ActaSancion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_incidente', models.DateField(verbose_name='Fecha del Incidente')),
                ('descripcion_incidente', models.CharField(max_length=500, verbose_name='Descripción del Incidente')),
                ('acta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actasancion', to='actas.Acta', verbose_name='Acta')),
            ],
            options={
                'verbose_name': 'Sanción',
                'verbose_name_plural': 'Sanciones',
            },
        ),
        migrations.CreateModel(
            name='Ascenso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acta_ascenso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ascenso', to='bomberos.ActaAscenso', verbose_name='Acta Ascenso')),
            ],
            options={
                'ordering': ['acta_ascenso'],
            },
        ),
        migrations.CreateModel(
            name='Bombero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Foto Carnet')),
                ('numero_credencial', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Número de Credencial')),
                ('fecha_vencimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Vencimiento')),
                ('estado_civil', models.CharField(blank=True, choices=[('Casado', 'Casado/a'), ('Concubino', 'Concubino/a'), ('Divorciado', 'Divorciado/a'), ('Separado', 'Separado/a'), ('Soltero', 'Soltero/a'), ('Viudo', 'Viudo/a')], default='Casado', max_length=255, null=True, verbose_name='Estado Civil')),
                ('lugar_nacimiento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='localidades.Localidad', verbose_name='Lugar de Nacimiento')),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bomberos', to='personas.Persona', verbose_name='Persona')),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bomberos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CalificacionAnual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.IntegerField(unique=True, verbose_name='Año')),
                ('puntaje_en_numero', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Puntaje Numérico')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bombero_calificacion', to='bomberos.Bombero', verbose_name='Bombero')),
            ],
        ),
        migrations.CreateModel(
            name='Empleo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título o cargo')),
                ('periodo_desde', models.DateField(verbose_name='Fecha de Inicio')),
                ('periodo_hasta', models.DateField(blank=True, null=True, verbose_name='Fecha de Fin')),
                ('descripcion', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Descripción')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bomberos.Bombero', verbose_name='Bombero')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Institucion', verbose_name='Empresa')),
            ],
            options={
                'verbose_name': 'Empleo',
                'verbose_name_plural': 'Empleos',
            },
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(choices=[('P', 'Primario'), ('S', 'Secundario'), ('T', 'Terciario'), ('U', 'Universitario')], default='P', max_length=5, verbose_name='Nivel de Estudio')),
                ('estado', models.CharField(choices=[('F', 'Finalizado'), ('C', 'Cursando'), ('A', 'Abandonado')], default='F', max_length=5, verbose_name='Estado de cursado')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('periodo_desde', models.DateField(verbose_name='Fecha de Inicio')),
                ('periodo_hasta', models.DateField(blank=True, null=True, verbose_name='Fecha de Fin')),
                ('descripcion', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Descripción')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bomberos.Bombero', verbose_name='Bombero')),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Institucion', verbose_name='Establecimiento')),
            ],
            options={
                'verbose_name': 'Estudio',
                'verbose_name_plural': 'Estudios',
            },
        ),
        migrations.CreateModel(
            name='Licencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_desde', models.DateField(verbose_name='Fecha desde')),
                ('fecha_hasta', models.DateField(verbose_name='Fecha hasta')),
                ('motivo', models.CharField(max_length=500, verbose_name='Motivo de la Licencia')),
                ('acta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acta_licencia', to='actas.Acta', verbose_name='Acta')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bombero_licenciado', to='bomberos.Bombero', verbose_name='Bombero')),
            ],
            options={
                'verbose_name': 'Licencia',
                'verbose_name_plural': 'Licencias',
            },
        ),
        migrations.CreateModel(
            name='NumeroOrden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_orden', models.SmallIntegerField(verbose_name='Número de Orden')),
                ('vigencia_desde', models.DateField(default=django.utils.timezone.now)),
                ('vigencia_hasta', models.DateField(blank=True, null=True)),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numeros_orden_bombero', to='bomberos.Bombero', verbose_name='Bombero')),
            ],
            options={
                'verbose_name': 'Número de Orden',
                'verbose_name_plural': 'Números de Orden',
            },
        ),
        migrations.CreateModel(
            name='Parentesco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentesco', models.CharField(choices=[('Hermano', 'Hermano/a'), ('Padre', 'Padre'), ('Madre', 'Madre'), ('Hijo', 'Hijo/a'), ('Abuelo', 'Abuelo/a'), ('Nieto', 'Nieto/a'), ('Tio', 'Tío/a'), ('Primo', 'Primo/a'), ('Esposo', 'Esposo/a')], default='Hermano', max_length=255, verbose_name='Parentesco')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bombero', to='bomberos.Bombero', verbose_name='Bombero')),
                ('familiar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to='personas.Persona', verbose_name='Familiar')),
            ],
        ),
        migrations.CreateModel(
            name='Pase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_efectiva', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha efectiva del pase')),
                ('fecha_ult_ascenso', models.DateField(verbose_name='Fecha último ascenso')),
                ('fecha_bombero', models.DateField(blank=True, null=True, verbose_name='Fecha ascenso a Bombero')),
                ('acta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acta_pase', to='actas.Acta', verbose_name='Acta')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bombero_solicitante', to='bomberos.Bombero', verbose_name='Bombero solicitante')),
                ('grado_final', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grado_tomado_solicitante', to='grados.Grado', verbose_name='Grado asignado al solicitante')),
                ('grado_origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grado_solicitante', to='grados.Grado', verbose_name='Grado del solicitante')),
                ('institucion_destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institucion_destino', to='personas.Institucion', verbose_name='Institución Destino')),
                ('institucion_origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institucion_origen', to='personas.Institucion', verbose_name='Institución Origen')),
            ],
            options={
                'verbose_name': 'Pase',
                'verbose_name_plural': 'Pases',
            },
        ),
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_premiacion', models.DateField(verbose_name='Fecha de la premiación')),
                ('premio_otorgado', models.CharField(max_length=500, verbose_name='Premio Otorgado')),
                ('acta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acta_premio', to='actas.Acta', verbose_name='Acta')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bombero_premiado', to='bomberos.Bombero', verbose_name='Bombero premiado')),
            ],
            options={
                'verbose_name': 'Premio',
                'verbose_name_plural': 'Premios',
            },
        ),
        migrations.CreateModel(
            name='Renuncia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateField(blank=True, null=True, verbose_name='Fecha de solicitud de baja')),
                ('fecha_efectiva', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha efectiva de baja')),
                ('acta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acta_renuncia', to='actas.Acta', verbose_name='Acta')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bombero_baja', to='bomberos.Bombero', verbose_name='Bombero dado de baja')),
            ],
            options={
                'verbose_name': 'Renuncia',
                'verbose_name_plural': 'Renuncia',
            },
        ),
        migrations.CreateModel(
            name='Sancion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_incidente', models.CharField(max_length=1000, verbose_name='Rol que cumplió en el incidente')),
                ('descargo', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Descargo presentado por el Bombero')),
                ('tipo_sancion', models.CharField(choices=[('advertencia', 'Advertencia'), ('suspencion', 'Suspención'), ('baja', 'Baja'), ('exoneracion', 'Exoneración')], default='advertencia', max_length=20, verbose_name='Tipo de Sanción disciplinaria')),
                ('dias_suspencion', models.SmallIntegerField(default=0, verbose_name='Días de Suspención')),
                ('fecha_efectiva', models.DateField(blank=True, null=True, verbose_name='Fecha en que se efectiviza la sanción')),
                ('acta_sancion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acta_sancion', to='bomberos.ActaSancion', verbose_name='Acta de Sanción')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bombero_interviniente', to='bomberos.Bombero', verbose_name='Bombero interviniente')),
            ],
            options={
                'ordering': ['acta_sancion'],
            },
        ),
        migrations.AddField(
            model_name='ascenso',
            name='bombero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bombero_ascendido', to='bomberos.Bombero', verbose_name='Bombero Ascendido'),
        ),
        migrations.AddField(
            model_name='ascenso',
            name='grado_ascenso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grado_ascendido', to='grados.Grado', verbose_name='Grado Ascendido'),
        ),
    ]
