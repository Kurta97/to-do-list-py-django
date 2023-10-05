from django.contrib import admin

from todo.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Task)
class DishAdmin(admin.ModelAdmin):
    list_display = ["content", "create", "deadline", "status"]
    list_filter = ["status"]
    search_fields = ["status"]
