from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Get user by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']  # pk - primary key
        # user = User.objects.get(id=pk)  # Вызовет ошибку, если такого id нет в таблице
        user = User.objects.filter(pk=pk).first()  # Вернет None в аналогичном случае
        self.stdout.write(f'{user}')
