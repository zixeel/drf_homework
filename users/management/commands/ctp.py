from django.core.management import BaseCommand

from materials.models import Course
from users.models import Payment, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.get(pk=1)
        paid_course = Course.objects.get(pk=3)
        payment = Payment.objects.create(
            user=user,
            paid_course=paid_course,
            payment_amount=4500,
            payment_method='CASHLESS'
        )
        payment.save()
