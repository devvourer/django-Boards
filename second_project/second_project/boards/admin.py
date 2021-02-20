from django.contrib import admin
from .models import *

# Register your models here.
class ImageInLineAdd(admin.TabularInline):
    model = PostImage
    fields = ('image',)
    max_num = 5

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInLineAdd,]
    list_filter = ('created_by', 'created_at')



admin.site.register(Board)
admin.site.register(Topic)

