from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'plant', 'quantity', 'status', 'created_at')
    search_fields = ('user__username', 'plant__name')
    list_filter = ('status', 'user')
