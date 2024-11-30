from django.contrib import admin

from .models import Aluno, Curso


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'curso')
    search_fields = ('nome', 'matricula')
    list_filter = ('curso',)


class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Curso, CursoAdmin)
