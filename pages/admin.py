from django.contrib import admin

#importar modelos
from .models import Page

# Register your models here.

#configuracion extra

class PageAdmin(admin.ModelAdmin):
    readonly_fields=("created_at","update_at")
    search_fields=('title','content')
    list_filter=('visible',)
    list_display=('title','visible','created_at')
    ordering=('-created_at',)
# Register your models here.
    
    
#REGISTRO DE APP "PAGES"
admin.site.register(Page,PageAdmin)

#Panel de gestion - TITULOS - SUBTITULOS
title='Gestion de Mediciones'
subtitle='Panel de Gestion'


admin.site.site_header=title
admin.site.site_title=title
admin.site.index_title=subtitle