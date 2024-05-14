from django.core.management import BaseCommand

from users.models import Payment


class Command(BaseCommand):
    def handle(self, *args, **options):
        payment = Payment.objects.create(
            user=1,
            paid_course=2,
            payment_amount=2500,
            payment_method='CASH'
        )
        payment.save()
