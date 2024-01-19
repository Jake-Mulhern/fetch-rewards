from django.contrib import admin
from .models import Receipt, Item

class ItemInline(admin.TabularInline):
   model = Item
   extra = 1

class ReceiptAdmin(admin.ModelAdmin):
   inlines = [ItemInline,]

admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(Item)