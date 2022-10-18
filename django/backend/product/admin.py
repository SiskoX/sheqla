from django.contrib import admin

# Register your models here.
from .models import Category,Product
from mptt.admin import MPTTModelAdmin

class CategoryMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20
admin.site.register(Category,CategoryMPTTModelAdmin)
admin.site.register(Product)