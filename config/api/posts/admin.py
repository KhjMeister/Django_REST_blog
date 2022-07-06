from django.contrib import admin
from .models import Post
  

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'body','active' , 'created_at', 'updated_at')
    list_filter = ('title', 'author','active', 'created_at', 'updated_at')
    search_fields = ('title', 'author', 'created_at',)
    
    list_per_page = 20
    actions = ['approve_post']

    def approve_post(self, request, queryset):
        queryset.update(active=True)