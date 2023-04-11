from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from tag.models import Tag
from django.contrib.auth import get_user_model

CREATE_LIST_TAG = reverse('create_get_list_tag')
UPDATE_GET_DELETE_TAG_URL_STRING = 'get_update_delete_tag'
class TestForTagApi(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="fighting_game_freak@ur_mom.com",
            password="3rdStrikeIsBESTGAME!!@@@!##@",
            is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_create_tag(self):
        name_of_created = "fighting"
        payload = {
            "name": name_of_created
        }
        response_from_creating_tag = self.client.post(CREATE_LIST_TAG, payload)
        self.assertEqual(response_from_creating_tag.status_code, status.HTTP_201_CREATED)

    def test_delete_tag(self):
        payload = {
            "name": "tag_to_delete"
        }

        response_from_creating_tag = self.client.post(CREATE_LIST_TAG, payload)
        id_of_created_tag = response_from_creating_tag.data['id']
        response_from_deleting_tag = self.client.delete(reverse(UPDATE_GET_DELETE_TAG_URL_STRING, kwargs={'pk': id_of_created_tag}))
        self.assertEqual(response_from_deleting_tag.status_code, status.HTTP_204_NO_CONTENT)

        response_from_attempting_to_get_deleted_tag = self.client.get(reverse(UPDATE_GET_DELETE_TAG_URL_STRING, kwargs={'pk': id_of_created_tag}))
        self.assertEqual(response_from_attempting_to_get_deleted_tag.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_tag(self):
        misspelt_name_of_created_tag = 'abventure'
        correct_name_of_created_tag = 'adventure'
        post_payload = {
            "name": misspelt_name_of_created_tag
        }
        response_from_creating_tag = self.client.post(CREATE_LIST_TAG, post_payload)
        id_of_created_tag = response_from_creating_tag.data['id']
        self.assertEqual(response_from_creating_tag.status_code, status.HTTP_201_CREATED)
        put_payload = {
            "name": correct_name_of_created_tag
        }
        response_from_editing_tag = self.client.put(reverse(UPDATE_GET_DELETE_TAG_URL_STRING, kwargs={'pk': id_of_created_tag}), put_payload)
        self.assertEqual(response_from_editing_tag.status_code, status.HTTP_200_OK)

        tag_obj = Tag.objects.get(id=id_of_created_tag)
        self.assertEqual(tag_obj.name, correct_name_of_created_tag)

