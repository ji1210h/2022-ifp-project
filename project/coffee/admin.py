from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from coffee.models import *
from coffee.forms import UserChangeForm, UserCreationForm
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title','material_list', 'image','create_dt', 'update_dt', 'bookmark_list')

    def category_list(self, obj):
        return ','.join([t.name for t in obj.category.all()])

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('category')
    
    def bookmark_list(self, obj):
        return ','.join([t.username for t in obj.bookmark_user.all()])
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('bookmark_user')
    
    def material_list(self, obj):
        return ','.join([t.name for t in obj.material.all()])
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('material')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email','profile_image','username', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email','profile_image','username', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','profile_image','username', 'date_of_birth', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)