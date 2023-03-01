"""
Tests for custom management commands in Django
"""
from django.test import SimpleTestCase
from django.core.management import call_command
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2Error
from unittest.mock import patch

@patch("core.management.commands.wait_for_db.Command.check")
class CommandTests(SimpleTestCase):
    """
    Test Commands
    """
    def test_if_waits_for_db_available(self, patched_check):
        """Test if waiting for database to be ready and available"""
        patched_check.return_value = True
        call_command('wait_for_db')
        patched_check.assert_called_once_with(databases=["default"])

    @patch('time.sleep')
    def test_if_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test if waiting for database when encountering OperationalError"""
        patched_check.side_effect = [OperationalError] * 3 + [Psycopg2Error] * 2 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])