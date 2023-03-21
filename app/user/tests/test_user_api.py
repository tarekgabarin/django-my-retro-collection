"""
Test for User endpoints
"""
from rest_framework import status
from rest_framework.test import APIClient

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase


CREATE_USER_URL = reverse('user:create')

def create_user_account(**params):
    return get_user_model().objects.create_user(**params)

class TestsForPublicUserApi(TestCase):
    """Tests for the public-facing features of the user API"""
    def setUp(self):
        self.client = APIClient()

    def test_if_can_successfully_create_user(self):
        payload = {
            "email": "johndoe@testingemailstuff.com",
            "password": "rocketSock@#12",
            "name": "John Doe"
        }
        response_from_post_request = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(response_from_post_request.status_code, status.HTTP_201_CREATED)
        
        created_user = get_user_model().objects.get(email=payload['email'])
        does_created_user_exist_in_db = get_user_model().objects.filter(email=payload['email']).exists()
        self.assertTrue(does_created_user_exist_in_db)

        self.assertTrue(created_user.check_password(payload['password']))
        self.assertNotIn('password', response_from_post_request.data)

    def test_if_cannot_create_user_if_email_already_exists(self):
        """Test if error is returned if a created user with a given email already exists"""
        payload = {
            "email": "johndoe@testingemailstuff.com",
            "password": "Testingthisstuffout123!@#",
            "name": "John Doe"
        }
        create_user_account(**payload)
        response_from_post_request = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(response_from_post_request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_entered_password_is_too_short(self):
        """Test if error thrown if entered password is too short (less than 5 chars)"""
        payload = {
            "email": "myemail@test.com",
            "password": "pw1",
            "name": "John Doe"
        }
        response_from_post_request = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(response_from_post_request.status_code, status.HTTP_400_BAD_REQUEST)
        
        does_user_with_short_password_exists = get_user_model().objects.filter(email=payload['email']).exists()
        self.assertFalse(does_user_with_short_password_exists)
    
    def test_if_no_lowercase_in_entered_password(self):
        """
        Test if validation error thrown if entered password has no lowercase characters
        """
        no_lowercase_payload = {
            "email": "myvalidator@test.com",
            "password": "TESTINGSTUFF!3",
            "name": "John Doe"
        }
        response_no_lowercase = self.client.post(CREATE_USER_URL, no_lowercase_payload)
        self.assertEqual(response_no_lowercase.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_no_uppercase_in_entered_password(self):
        """
        Test if validation error thrown if entered password has no uppercase characters
        """
        no_uppercase_payload = {
            "email": "myvalidator@test.com",
            "password": "testingstuff!3",
            "name": "John Doe"
        }
        response_no_uppercase = self.client.post(CREATE_USER_URL, no_uppercase_payload)
        self.assertEqual(response_no_uppercase.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_no_digits_in_entered_password(self):
        """
        Test if validation error thrown if entered password has no digit characters
        """
        no_digits_payload = {
            "email": "myvalidator@test.com",
            "password": "testingstuff!",
            "name": "John Doe"
        }
        response_no_digits = self.client.post(CREATE_USER_URL, no_digits_payload)
        self.assertEqual(response_no_digits.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_no_special_char_in_entered_password(self):
        """
        Test if validation error thrown if entered password has no digit characters
        """
        no_special_char_payload = {
            "email": "myvalidator@test.com",
            "password": "testingstuff3",
            "name": "John Doe"
        }
        response_no_special_char = self.client.post(CREATE_USER_URL, no_special_char_payload)
        self.assertEqual(response_no_special_char.status_code, status.HTTP_400_BAD_REQUEST)





