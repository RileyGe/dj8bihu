from django.contrib import admin
from gs8bihu.models import RecommendAuthor


# Register your models here.
class RecommendAuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'info', 'icon', 'artnum', 'fans', 'order']


admin.site.register(RecommendAuthor, RecommendAuthorAdmin)
