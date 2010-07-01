from geonode.maps.models import Map, Layer, MapLayer, Contact, Role
from django.contrib import admin

class MapLayerInline(admin.TabularInline):
    model = MapLayer

class RoleInline(admin.TabularInline):
    model = Role

class RoleAdmin(admin.ModelAdmin):
    model = Role
    list_display_links = ('id',)
    list_display = ('id','contact', 'layer', 'value')
    list_editable = ('contact', 'layer', 'value')

class MapAdmin(admin.ModelAdmin):
    inlines = [MapLayerInline,]

class ContactAdmin(admin.ModelAdmin):
    inlines = [RoleInline]

class LayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'typename','title', 'date', 'constraints_use', 'topic_category')
    list_display_links = ('id',)
    list_editable = ('title', 'constraints_use', 'topic_category')
    list_filter  = ('date', 'date_type', 'constraints_use', 'topic_category')
    filter_horizontal = ('contacts',)
    date_hierarchy = 'date'
    readonly_fields = ('uuid', 'typename', 'workspace') 
    inlines = [RoleInline]

admin.site.register(Map, MapAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Layer, LayerAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(MapLayer)
