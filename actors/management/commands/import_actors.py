import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from actors.models import Actors


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com atores',
        )

# a função acima funciona para que ao chamar no terminal o comando, possa se adicionar um argumento
# que nesse caso é um nome de arquivo csv que vai ser lido    

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(name))

                Actors.objects.create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality,
                )

        self.stdout.write(self.style.SUCCESS('ATORES IMPORTADOS COM SUCESSO'))
