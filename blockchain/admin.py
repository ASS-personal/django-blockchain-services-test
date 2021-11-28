from django.contrib import admin
from blockchain.models import L3BTCUSDAsks, L3BTCUSDBids

@admin.register(L3BTCUSDAsks)
class L3BTCUSDAsksAdmin(admin.ModelAdmin):
    list_display = ['num', 'px', 'qty', 'value']

@admin.register(L3BTCUSDBids)
class L3BTCUSDBidsAdmin(admin.ModelAdmin):
    list_display = ['num', 'px', 'qty', 'value']