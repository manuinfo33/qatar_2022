from django.contrib import admin
from news.models import Articles

@admin.register(Articles)
class Articles_admin(admin.ModelAdmin):
    list_display = ['title','creation_date','author']