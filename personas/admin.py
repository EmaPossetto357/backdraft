# -*- coding: UTF-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext as _
from personas.models import (
    Persona,
    Bombero,
    DireccionPostal,
    DireccionWeb,
    Telefono,
    DireccionElectronica,
    Parentesco,
    Estudio,
    Empleo,
    Institucion,
    CalificacionAnual,
    Cuartelero,
)


@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'tipo_cuit',
                'nro_cuit',
                'razon_social',
                )
        }),
    )
    list_display = (
        'tipo_cuit',
        'nro_cuit',
        'razon_social',
    )
    search_fields = (
        'nro_cuit',
        'razon_social',
    )


@admin.register(Estudio)
class EstudioAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'bombero',
                'establecimiento',
                'nivel',
                'titulo',
                'estado',
                'periodo_desde',
                'periodo_hasta',
                )
        }),
        (_('Descripcion'), {
            'classes': ('collapse',),
            'fields': ('descripcion',),
        }),
    )
    list_display = (
        'periodo',
        'establecimiento',
        'bombero',
    )
    search_fields = (
        'bombero__persona__apellido',
        'bombero__persona__nombre',
        'bombero__persona__documento',
        'bombero__persona__nro_cuit',
        'establecimiento__razon_social',
        'establecimiento__nro_cuit',
        'nivel',
        'estado',
        'titulo',
    )
    list_filter = (
        'bombero',
        'establecimiento',
        'nivel',
        'estado',
        'titulo',
    )
    date_hierarchy = 'periodo_desde'

    def periodo(self, obj):
        return obj.periodo
    periodo.short_description = _('Periodo')


@admin.register(Empleo)
class EmpleoAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'bombero',
                'empresa',
                'titulo',
                'periodo_desde',
                'periodo_hasta',
                )
        }),
        (_('Descripcion'), {
            'classes': ('collapse',),
            'fields': ('descripcion',),
        }),
    )
    list_display = (
        'periodo',
        'empresa',
        'bombero',
    )
    search_fields = (
        'bombero__persona__apellido',
        'bombero__persona__nombre',
        'bombero__persona__documento',
        'bombero__persona__nro_cuit',
        'empresa__razon_social',
        'empresa__nro_cuit',
        'titulo',
    )
    list_filter = (
        'bombero',
        'empresa',
    )
    date_hierarchy = 'periodo_desde'

    def periodo(self, obj):
        return obj.periodo
    periodo.short_description = _('Periodo')


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'tipo_cuit',
                'nro_cuit',
                'apellido',
                'nombre',
                'tipo_documento',
                'documento',
                'grupo_sanguineo',
                'factor_sanguineo',
                'fecha_nacimiento',
                'genero')
        }),
        (_('¿Fallecido?'), {
            'classes': ('collapse',),
            'fields': ('fecha_desceso',),
        }),
    )
    list_display = (
        'nombre_completo',
        'dni',
        'genero',
        'sangre',
        'fecha_nacimiento',
        'fecha_desceso',)
    search_fields = (
        'apellido',
        'nombre',
        'documento',
        'nro_cuit',
    )
    list_filter = (
        'apellido',
        'fecha_nacimiento',
        'tipo_documento',
        'genero',
        'grupo_sanguineo',
        'factor_sanguineo',
        'fecha_desceso',)
    date_hierarchy = 'fecha_nacimiento'


@admin.register(Cuartelero)
class CuarteleroAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'persona',),
        }),
    )
    list_display = (
        '__str__',
        'dni',
        'fecha_nacimiento',
        'sangre',
    )
    search_fields = (
        'persona__apellido',
        'persona__nombre',
        'persona__documento',
        'persona__nro_cuit',
    )
    list_filter = (
        'persona__apellido',
        'persona__fecha_nacimiento',
        'persona__tipo_documento',
        'persona__genero',
        'persona__grupo_sanguineo',
        'persona__factor_sanguineo',
        'persona__fecha_desceso',
    )


@admin.register(Bombero)
class BomberoAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'persona',
                'numero_credencial',
                'fecha_vencimiento',
                'foto',
                'estado_civil',
                'lugar_nacimiento',
                )
        }),
    )
    list_display = (
        'nro_legajo',
        'numero_credencial',
        'fecha_vencimiento',
        'nombre_completo',
        'dni',
        'sangre',
        'get_grado_ultimo_ascenso',
        'antiguedad_bombero',
    )

    def nro_legajo(self, obj):
        return obj.pk
    nro_legajo.short_description = _('Legajo')

    def nombre_completo(self, obj):
        return obj.persona.nombre_completo
    nombre_completo.short_description = _('Apellido y Nombre')

    def sangre(self, obj):
        return obj.persona.sangre
    sangre.short_description = _('Grupo Sanguíneo')

    def dni(self, obj):
        return obj.persona.dni
    dni.short_description = _('Documento')

    def get_grado_ultimo_ascenso(self, obj):
        try:
            return obj.get_grado_ultimo_ascenso.nombre
        except AttributeError:
            return None
    get_grado_ultimo_ascenso.short_description = _("Grado")

    def antiguedad_bombero(self, obj):
        return _("{} años").format(
            obj.antiguedad_bombero,
        )
    antiguedad_bombero.short_description = _("Antigüedad como Bombero")

    search_fields = (
        'persona__apellido',
        'persona__nombre',
        'persona__documento',
        'persona__nro_cuit',
    )
    list_filter = (
        'persona__apellido',
        'persona__fecha_nacimiento',
        'persona__tipo_documento',
        'persona__genero',
        'persona__grupo_sanguineo',
        'persona__factor_sanguineo',
        'persona__fecha_desceso',
    )


@admin.register(Parentesco)
class ParentescoAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_display = (
        'bombero',
        'familiar',
        'parentesco',)
    search_fields = (
        'bombero.persona.apellido',
        'bombero.persona.nombre',
        'familiar.apellido',
        'familiar.nombre',)


@admin.register(DireccionPostal)
class DireccionPostalAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'entidad',
                'uso',
                'calle',
                'numero',
                'piso',
                'departamento',
                'localidad')
            }),
        (_("Observaciones"), {
            'classes': ('collapse',),
            'fields': ('observaciones',),
            }))
    search_fields = (
        'calle',
        'numero',
        'piso',
        'departamento',
        'localidad__nombre')
    list_display = (
        'entidad',
        'direccion_completa',
    )
    list_filter = (
        'entidad',
        'uso',
        'localidad')


@admin.register(DireccionWeb)
class DireccionWebAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'entidad',
                'tipo',
                'uso',
                'direccion')
            }),
        (_("Observaciones"), {
            'classes': ('collapse',),
            'fields': ('observaciones',),
            }))
    list_display = (
        'entidad',
        'tipo',
        'uso',
        'direccion')
    list_filter = (
        'entidad',
        'tipo',
        'uso')


@admin.register(Telefono)
class TelefonoAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'entidad',
                'tipo',
                'uso',
                'telefono')
            }),
        (_("Observaciones"), {
            'classes': ('collapse',),
            'fields': ('observaciones',),
            }))
    list_display = (
        'entidad',
        'tipo',
        'uso',
        'telefono',)
    list_filter = (
        'entidad',
        'tipo',
        'uso')


@admin.register(DireccionElectronica)
class DireccionElectronicaAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'entidad',
                'mail',)
            }),
        (_("Observaciones"), {
            'classes': ('collapse',),
            'fields': ('observaciones',),
            }))
    list_display = (
        'entidad',
        'mail',)
    list_filter = (
        'entidad',)


@admin.register(CalificacionAnual)
class CalificacionAnualAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_display = (
        'bombero',
        'periodo',
        'puntaje_en_numero',)
    list_filter = (
        'bombero',
        'periodo',)
    fieldsets = (
        (None, {
            'fields': (
                'bombero',
                'periodo',
                'puntaje_en_numero',)
        }),
    )
