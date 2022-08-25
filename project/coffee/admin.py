from django.contrib import admin
from coffee.models import *
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'tag_list', 'title','material_list', 'image','create_dt', 'update_dt', 'bookmark_list')

    def tag_list(self, obj):
        return ','.join([t.name for t in obj.tags.all()])
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    
    def bookmark_list(self, obj):
        return ','.join([t.username for t in obj.bookmark.all()])
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('bookmark')
    
    def material_list(self, obj):
        return ','.join([t.name for t in obj.material.all()])
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('material')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')