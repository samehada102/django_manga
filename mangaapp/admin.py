from django.contrib import admin
# models.pyの読み込み
from .models import Item

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass