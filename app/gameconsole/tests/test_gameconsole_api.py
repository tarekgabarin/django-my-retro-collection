from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from gameconsole.models import GameConsole
from django.contrib.auth import get_user_model
from consolemaker.tests.factories import ConsoleMakerFactory
from gameconsole.tests.factories import GameConsoleFactory
import json

URL_FOR_POST_LIST_GAME_CONSOLE = reverse("gameconsole-list")
URL_FOR_PUT_DETAIL_GAME_CONSOLE = "gameconsole-detail"


class TestsForConsoleMaker(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="fighting_game_freak@ur_mom.com",
            password="3rdStrikeIsBESTGAME!!@@@!##@",
            is_staff=True,
        )
        self.client.force_authenticate(self.user)

    def convert_ordered_dict_to_list(self, arr_of_ordered_dicts):
        return [
            json.loads(json.dumps(ordered_dicts))
            for ordered_dicts in arr_of_ordered_dicts
        ]

    @classmethod
    def setUpTestData(cls):
        """Brands for console manfucaturers"""
        cls.nintendo_brand = ConsoleMakerFactory(name="nintendo")
        cls.sega_brand = ConsoleMakerFactory(name="sega")
        cls.sony_brand = ConsoleMakerFactory(name="sony")
        cls.microsoft_brand = ConsoleMakerFactory(name="microsoft")

        """Video game consoles"""
        cls.genesis_console = GameConsoleFactory(
            name="Genesis", maker_of_console=cls.sega_brand, name_code="MD"
        )
        cls.super_nes_console = GameConsoleFactory(
            name="Super Nintendo", maker_of_console=cls.nintendo_brand, name_code="SNES"
        )
        cls.psx_console = GameConsoleFactory(
            name="Playstation", maker_of_console=cls.sony_brand, name_code="PSX"
        )
        cls.dc_console = GameConsoleFactory(
            name="Dreamcast", maker_of_console=cls.sega_brand, name_code="DC"
        )
        cls.windows_console = GameConsoleFactory(
            name="Windows", maker_of_console=cls.microsoft_brand, name_code="WIN"
        )

    def test_create_gameconsole(self):
        payload = {
            "console_maker_id": self.microsoft_brand.id,
            "name": "Xbox",
            "name_code": "XB",
        }
        response_from_create = self.client.post(URL_FOR_POST_LIST_GAME_CONSOLE, payload)
        self.assertEqual(response_from_create.status_code, status.HTTP_201_CREATED)

    def test_get_list_gameconsole(self):
        response_from_get_list = self.client.get(URL_FOR_POST_LIST_GAME_CONSOLE)
        consoles_found_in_query = self.convert_ordered_dict_to_list(
            response_from_get_list.data
        )
        self.assertEqual(response_from_get_list.status_code, status.HTTP_200_OK)
        self.assertEqual(len(consoles_found_in_query), 5)

    def test_update_game_console(self):
        incorrect_name = "Xbone"
        correct_name = "Xbox"
        payload = {
            "console_maker_id": self.microsoft_brand.id,
            "name": incorrect_name,
            "name_code": "XB",
        }
        response_from_create = self.client.post(URL_FOR_POST_LIST_GAME_CONSOLE, payload)
        id_of_created_console = response_from_create.data["id"]
        self.assertEqual(response_from_create.status_code, status.HTTP_201_CREATED)

        put_payload = {
            "console_id": id_of_created_console,
            "console_maker_id": self.microsoft_brand.id,
            "name": correct_name,
            "name_code": "XB",
        }
        response_from_put = self.client.put(
            reverse(URL_FOR_PUT_DETAIL_GAME_CONSOLE, args=[id_of_created_console]),
            put_payload,
        )
        self.assertEqual(response_from_put.status_code, status.HTTP_200_OK)

        is_name_still_incorrect = GameConsole.objects.filter(
            name=incorrect_name
        ).exists()
        self.assertEqual(is_name_still_incorrect, False)
