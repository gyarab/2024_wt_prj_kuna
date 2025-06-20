from django.contrib import admin
from .models import Cryptocurrency, CryptoType, UserWatchlist
# Register your models here.
@admin.register(Cryptocurrency)
class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'type')
    list_filter = ('type',)
    search_fields = ('name', 'symbol')

@admin.register(CryptoType)
class CryptoTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(UserWatchlist)
class UserWatchlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'cryptocurrency')
    list_filter = ('user',)
    search_fields = ('user__username', 'cryptocurrency__name')
