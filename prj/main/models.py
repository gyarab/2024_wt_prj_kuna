from django.db import models
from django.contrib.auth.models import User 


class Cryptocurrency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)  # např. BTC
    description = models.TextField()
    type = models.ForeignKey("CryptoType", on_delete=models.SET_NULL, null=True)


class PriceRecord(models.Model):
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
    price_usd = models.DecimalField(max_digits=20, decimal_places=8)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.cryptocurrency.symbol} - {self.price_usd} USD @ {self.timestamp}"

class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'cryptocurrency')  # Každý uživatel si může přidat každou měnu jen jednou

    def __str__(self):
        return f"{self.user.username} likes {self.cryptocurrency.symbol}"

class CryptoType(models.Model):
    name = models.CharField(max_length=100)  # např. memecoin, gaming, etc.

class UserWatchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)

