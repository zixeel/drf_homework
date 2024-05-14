from django.core.management import BaseCommand

from users.models import User, Payment


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.ru',
            phone='111',
            country='Кадия',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('5682')
        user.save()



