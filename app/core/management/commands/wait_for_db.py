"""
Django command to ensure the database is available when Django starts
"""
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

class Command(BaseCommand):
    """Django command to wait for the database to be available"""

    def handle(self, *args, **options):
        is_database_up = False
        self.stdout.write("Waiting for database...")
        while is_database_up is False:
            try:
                self.check(databases=['default'])
                is_database_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database up and running!'))