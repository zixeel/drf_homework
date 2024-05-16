from django.core.management import BaseCommand

from materials.models import Course
from users.models import User, Payment


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin4@mail.ru',
            phone='1112',
            country='Кадия',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('5682')
        user.save()

        course = Course.objects.create(
            name='drf-3',
            description='some text'
        )
        course.save()

        paid_course = course
        payment = Payment.objects.create(
            user=user,
            paid_course=paid_course,
            payment_amount=5500,
            payment_method='CASHLESS'
        )
        payment.save()
