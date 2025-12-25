from django.contrib import admin
from .models import Todo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'Status', 'user')
    list_filter = ('Status', 'user')
    search_fields = ('title', 'due_date', 'Status', 'user')
    ordering = ('-created_at',)

admin.site.register(Todo, TodoAdmin)