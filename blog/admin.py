from django.contrib import admin

# Register your models here.
from .models import Post,Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('created','publish','author','status')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
admin.site.register(Post,PostAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','email','created','post','active')
    list_filter = ('created','name','active')
    search_fields = ('body','name','email')
    ordering = ['created','active']
admin.site.register(Comment,CommentsAdmin)





