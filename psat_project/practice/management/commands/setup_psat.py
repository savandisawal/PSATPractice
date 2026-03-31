"""
Management command: python manage.py setup_psat

Runs migrations, loads fixtures, and provides setup guidance.
"""
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Set up the PSAT Practice site: run migrations and load sample data.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING('\n=== PSAT Practice Setup ===\n'))

        self.stdout.write('Running migrations...')
        call_command('migrate', verbosity=1)

        self.stdout.write('Loading sample questions and subjects...')
        call_command('loaddata', 'initial_data', verbosity=1)

        self.stdout.write(self.style.SUCCESS(
            '\n✓ Setup complete!\n\n'
            'Next steps:\n'
            '  1. Create a superuser:  python manage.py createsuperuser\n'
            '  2. Start the server:    python manage.py runserver\n'
            '  3. Visit:               http://localhost:8000\n'
            '  4. Admin panel:         http://localhost:8000/admin\n'
        ))
