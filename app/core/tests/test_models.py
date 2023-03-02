"""
Testing for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test Models"""

    def test_if_create_user_with_email_successful(self):
        """Test if can successfully create a user with an email"""

        test_password = "testing123"
        test_email = "example@test.com"
        
        test_user = get_user_model().objects.create_user(
            email=test_email,
            password=test_password
        )

        self.assertEqual(test_user.email, test_email)
        self.assertTrue(test_user.check_password(test_password))

    def test_if_created_user_email_normalized(self):
        """Test if the email of a newly-created user is normalized"""
        arr_of_test_sample_emails = [
            ["example@TEST.com", "example@test.com"],
            ['myemail@exAMPLE.com', 'myemail@example.com'],
            ['Example2@tEST.com', 'Example2@test.com']
        ]

        for inputted_email, expected in arr_of_test_sample_emails:
            created_user = get_user_model().objects.create_user(inputted_email, "testing123")
            self.assertEqual(created_user.email, expected)

    def test_if_creating_user_without_email_throws_error(self):
        """Test to see if creating a user without an email provided throws a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'testing123')

    def test_if_create_superuser(self):
        """Testing to see if a superuser can be created"""
        created_user = get_user_model().objects.create_superuser(
            'example@testing.com',
            'testing123'
        )

        self.assertTrue(created_user.is_superuser)
        self.assertTrue(created_user.is_staff)