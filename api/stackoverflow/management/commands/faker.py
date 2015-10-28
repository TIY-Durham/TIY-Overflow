from django.core.management.base import BaseCommand, CommandError

from stackoverflow import models

class Command(BaseCommand):
  help = 'Create fake data for the application'

  def add_arguments(self, parser):
    parser.add_argument('num_questions', type=int, nargs='?', default=50)
    parser.add_argument('answers_per_question', type=int, nargs='?', default=5)
    parser.add_argument('num_users', type=int, nargs='?', default=5)

  def handle(self, *args, **options):
    print(options)
    models.make_fake_data(
      options['num_questions'],
      options['answers_per_question'],
      options['num_users']
    )

