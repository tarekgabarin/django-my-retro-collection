from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from publisher.models import Publisher
from django.contrib.auth import get_user_model

CREATE_LIST_PUBLISHER = reverse('create_get_list_publisher')
UPDATE_GET_DELETE_PUBLISHER_URL_STRING = 'get_update_delete_publisher'
class TestForPublisherApi(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="fighting_game_freak@ur_mom.com",
            password="3rdStrikeIsBESTGAME!!@@@!##@",
            is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_create_publisher(self):
        name_of_created = "Falcom"
        payload = {
            "name": name_of_created
        }
        response_from_creating_publisher = self.client.post(CREATE_LIST_PUBLISHER, payload)
        self.assertEqual(response_from_creating_publisher.status_code, status.HTTP_201_CREATED)

    def test_delete_publisher(self):
        payload = {
            "name": "publisher_to_delete"
        }

        response_from_creating_publisher = self.client.post(CREATE_LIST_PUBLISHER, payload)
        id_of_created_publisher = response_from_creating_publisher.data['id']
        response_from_deleting_publisher = self.client.delete(reverse(UPDATE_GET_DELETE_PUBLISHER_URL_STRING, kwargs={'pk': id_of_created_publisher}))
        self.assertEqual(response_from_deleting_publisher.status_code, status.HTTP_204_NO_CONTENT)

        response_from_attempting_to_get_deleted_publisher = self.client.get(reverse(UPDATE_GET_DELETE_PUBLISHER_URL_STRING, kwargs={'pk': id_of_created_publisher}))
        self.assertEqual(response_from_attempting_to_get_deleted_publisher.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_tag(self):
        misspelt_name_of_created_publisher = 'Falcon'
        correct_name_of_created_publisher = 'Falcom'
        post_payload = {
            "name": misspelt_name_of_created_publisher
        }
        response_from_creating_publisher = self.client.post(CREATE_LIST_PUBLISHER, post_payload)
        id_of_created_publisher = response_from_creating_publisher.data['id']
        self.assertEqual(response_from_creating_publisher.status_code, status.HTTP_201_CREATED)
        put_payload = {
            "name": correct_name_of_created_publisher
        }
        response_from_editing_publisher = self.client.put(reverse(UPDATE_GET_DELETE_PUBLISHER_URL_STRING, kwargs={'pk': id_of_created_publisher}), put_payload)
        self.assertEqual(response_from_editing_publisher.status_code, status.HTTP_200_OK)

        publisher_obj = Publisher.objects.get(id=id_of_created_publisher)
        self.assertEqual(publisher_obj.name, correct_name_of_created_publisher)
