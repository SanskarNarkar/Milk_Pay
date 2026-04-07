from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db.models import Sum
from core.models import User, MilkEntry
from django.conf import settings
from twilio.rest import Client

class Command(BaseCommand):
    help = 'Sends monthly payout reports to farmers via WhatsApp'

    def handle(self, *args, **kwargs):
        # 1. Setup Twilio
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        # 2. Get last month's date range
        today = timezone.now().date()
        current_month = today.month
        current_year = today.year
        
        self.stdout.write(f"Calculating reports for Month: {current_month}/{current_year}...")

        # 3. Loop through all farmers
        farmers = User.objects.filter(is_farmer=True)
        
        for farmer in farmers:
            entries = MilkEntry.objects.filter(
                farmer=farmer,
                date__month=current_month,
                date__year=current_year
            )
            
            total_pay = entries.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
            total_liters = entries.aggregate(Sum('quantity'))['quantity__sum'] or 0
            
            if total_pay > 0:
                msg_body = (
                    f"🥛 *MilkPay Monthly Report*\n"
                    f"Hello {farmer.username},\n\n"
                    f"🗓 Month: {today.strftime('%B %Y')}\n"
                    f"✅ Total Milk: {total_liters} Liters\n"
                    f"💰 *Payout: ${total_pay}*\n\n"
                    f"Thank you for working with us!"
                )
                
                try:
                    # Note: Farmer phone must include country code e.g., +919876543210
                    message = client.messages.create(
                        from_=settings.TWILIO_WHATSAPP_NUMBER,
                        body=msg_body,
                        to=f'whatsapp:{farmer.phone}' 
                    )
                    self.stdout.write(self.style.SUCCESS(f"Sent to {farmer.username}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Failed to send to {farmer.username}: {e}"))
            else:
                self.stdout.write(f"Skipping {farmer.username} (No collection)")