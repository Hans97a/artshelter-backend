from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = "This command creates superuser"

    def handle(self, *args, **options):
        try:
            User.objects.get(username="artshelter_admin")
            self.stdout.write(self.style.SUCCESS("Superuser Exists"))
        except User.DoesNotExist:
            User.objects.create_superuser("artshelter_admin", "", "toy123456")
            self.stdout.write(self.style.SUCCESS("Superuser Created"))
