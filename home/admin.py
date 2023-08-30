import unicodedata
from django.contrib import admin

# Register your models here.
from .models import Category, Article, Feed

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_homepage','layout', 'ordering')
    # prepopulated_fields = {'slug':('name',)}
    list_filter = ["is_homepage","status", "layout"]
    search_fields = ["name"]

    class Media:
        js = ('my_admin/js/jquery.min.js', 'my_admin/js/urlify.js', 'my_admin/js/xregexp.min.js')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'ordering')
    # prepopulated_fields = {'slug':('name',)}
    list_filter = ["status", "special"]
    search_fields = ["name"]

    class Media:
        js = ('my_admin/js/jquery.min.js', 'my_admin/js/urlify.js', 'my_admin/js/xregexp.min.js')

class FeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'ordering')
    # prepopulated_fields = {'slug':('name',)}
    list_filter = ["status"]
    search_fields = ["name"]

    class Media:
        js = ('my_admin/js/jquery.min.js', 'my_admin/js/urlify.js', 'my_admin/js/xregexp.min.js')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Feed, FeedAdmin)

admin.site.site_header = "TRANG QUẢN TRỊ CỦA ADMINISTRATOR"