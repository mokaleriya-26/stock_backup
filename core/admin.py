from django.contrib import admin
from .models import LastSeenStock, StockHistory, Watchlist


@admin.register(LastSeenStock)
class LastSeenStockAdmin(admin.ModelAdmin):
    list_display = ('user', 'symbol', 'last_seen_price', 'updated_at')
    list_filter = ('symbol',)
    search_fields = ('user__username', 'symbol')


@admin.register(StockHistory)
class StockHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'symbol', 'price', 'timestamp')
    list_filter = ('symbol',)
    search_fields = ('user__username', 'symbol')
    ordering = ('-timestamp',)


@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'symbol', 'added_at')
    list_filter = ('symbol',)
    search_fields = ('user__username', 'symbol')
