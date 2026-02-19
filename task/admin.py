from django.contrib import admin
from .models import Task, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_completed', 'category')

    list_filter = ('is_completed', 'user', 'category')

    search_fields = ('title', 'user__username')

    list_editable = ('is_completed',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')