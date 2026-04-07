from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    is_farmer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    phone = models.CharField(max_length=11, blank=True)
    address = models.TextField(blank=True)



class RateConfig(models.Model):
    # Two separate rates now
    price_cow_fat = models.DecimalField(max_digits=5, decimal_places=2, default=6.00, verbose_name="Cow Rate")
    price_buffalo_fat = models.DecimalField(max_digits=5, decimal_places=2, default=8.00, verbose_name="Buffalo Rate")
    updated_at = models.DateTimeField(auto_now=True)

class MilkEntry(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries',limit_choices_to={'is_farmer': True})
    date = models.DateField(default=timezone.now)
    shift = models.CharField(max_length=10, choices=[('Morning', 'Morning'), ('Evening', 'Evening')])
    

          # ⭐ IMPORTANT
    

    # New Field: Milk Type
    milk_type = models.CharField(max_length=10, choices=[('Cow', 'Cow'), ('Buffalo', 'Buffalo')], default='Cow')
    
    fat = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.DecimalField(max_digits=5, decimal_places=2) # Liters
    
    # Auto-calculated fields
    rate_applied = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # 1. Get current rates
        config = RateConfig.objects.last()
        
        # 2. Decide which price to use
        if config:
            if self.milk_type == 'Buffalo':
                base_price = float(config.price_buffalo_fat)
            else:
                base_price = float(config.price_cow_fat)
        else:
            base_price = 8.0 # Fallback

        # 3. Calculate
        self.rate_applied = float(self.fat) * base_price
        self.total_amount = float(self.quantity) * self.rate_applied
        
        super().save(*args, **kwargs)