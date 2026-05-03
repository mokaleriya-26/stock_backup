from django.db import models
from django.contrib.auth.models import User


class LastSeenStock(models.Model):
    """Stores the last price a user saw for a given stock symbol.
    Used to detect price increases/decreases between views (auto alerts).
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='last_seen_stocks')
    symbol = models.CharField(max_length=20)
    last_seen_price = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'symbol')

    def __str__(self):
        return f"{self.user.username} — {self.symbol} @ {self.last_seen_price}"


class StockHistory(models.Model):
    """Records every time a user views/generates insights for a stock."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stock_history')
    symbol = models.CharField(max_length=20)
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user.username} viewed {self.symbol} @ {self.price} on {self.timestamp}"


class Watchlist(models.Model):
    """User's saved stocks watchlist. Enforces uniqueness per user per symbol."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist')
    symbol = models.CharField(max_length=20)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'symbol')
        ordering = ['symbol']

    def __str__(self):
        return f"{self.user.username} watches {self.symbol}"
