from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from game.models import Game
import datetime
from tag.tests.factories import TagFactory
from gameconsole.tests.factories import GameConsoleFactory
from consolemaker.tests.factories import ConsoleMakerFactory
from publisher.tests.factories import PublisherFactory
from game.tests.factories import GameFactory
import json

GET_COLLECTION_URL = reverse("my-collection")
GET_GAME_URL = reverse("get-games")
ADD_TO_COLLECTION_URL = reverse("add-collection")
REMOVE_FROM_COLLECTION_URL = reverse("remove-collection")


class TestsForPublicGameApi(TestCase):
    """Tests for the public-facing features of the Games API"""

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        """Tags for games"""
        cls.action_tag = TagFactory(name="action")
        cls.platformer_tag = TagFactory(name="platformer")

        cls.single_player_tag = TagFactory(name="single-player")
        cls.multi_player_tag = TagFactory(name="multi-player")

        cls.rpg_tag = TagFactory(name="rpg")
        cls.strategy_tag = TagFactory(name="strategy")
        cls.turn_based_tag = TagFactory(name="turn-based")

        cls.shooter_tag = TagFactory(name="shooter")
        cls.fps_tag = TagFactory(name="first-person-shooter")

        cls.two_dimensional_tag = TagFactory(name="2d")
        cls.three_dimensional_tag = TagFactory(name="3d")

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

        """Video game publishers"""
        cls.capcom_publisher = PublisherFactory(name="capcom")
        cls.konami_publisher = PublisherFactory(name="konami")
        cls.sega_publisher = PublisherFactory(name="sega")
        cls.square_publisher = PublisherFactory(name="square-enix")
        cls.Id_software_publisher = PublisherFactory(name="id-software")

        """Games (some of my actual favorite games ever)"""
        cls.castlevania_game = GameFactory(
            title="Super Castlevania 4",
            game_consoles_released_on=[cls.super_nes_console],
            release_date=datetime.date(1991, 12, 4),
            publisher_of_game=cls.konami_publisher,
            players_that_own_game=[],
            tags_for_game=[cls.action_tag, cls.platformer_tag, cls.two_dimensional_tag],
        )

        cls.megaman_game = GameFactory(
            title="Megaman X",
            game_consoles_released_on=[cls.super_nes_console],
            release_date=datetime.date(1993, 12, 17),
            publisher_of_game=cls.capcom_publisher,
            players_that_own_game=[],
            tags_for_game=[cls.action_tag, cls.platformer_tag, cls.two_dimensional_tag],
        )

        cls.ghouls_ghost_game = GameFactory(
            title="Ghouls 'n Ghosts",
            game_consoles_released_on=[cls.genesis_console],
            release_date=datetime.date(1989, 9, 17),
            publisher_of_game=cls.capcom_publisher,
            players_that_own_game=[],
            tags_for_game=[cls.action_tag, cls.platformer_tag, cls.two_dimensional_tag],
        )

        cls.contra_game = GameFactory(
            title="Contra: Hard Corps",
            game_consoles_released_on=[cls.genesis_console],
            release_date=datetime.date(1994, 8, 8),
            publisher_of_game=cls.konami_publisher,
            players_that_own_game=[],
            tags_for_game=[
                cls.action_tag,
                cls.platformer_tag,
                cls.two_dimensional_tag,
                cls.shooter_tag,
            ],
        )

        cls.final_fantasy_game = GameFactory(
            title="Final Fantasy Tactics",
            game_consoles_released_on=[cls.psx_console],
            release_date=datetime.date(1997, 6, 20),
            publisher_of_game=cls.square_publisher,
            players_that_own_game=[],
            tags_for_game=[
                cls.rpg_tag,
                cls.turn_based_tag,
                cls.strategy_tag,
                cls.three_dimensional_tag,
            ],
        )

        cls.shining_force_game = GameFactory(
            title="Shining Force",
            game_consoles_released_on=[cls.genesis_console],
            release_date=datetime.date(1992, 3, 20),
            publisher_of_game=cls.sega_publisher,
            players_that_own_game=[],
            tags_for_game=[
                cls.rpg_tag,
                cls.turn_based_tag,
                cls.strategy_tag,
                cls.three_dimensional_tag,
            ],
        )

        cls.chrono_trigger_game = GameFactory(
            title="Chrono Trigger",
            game_consoles_released_on=[cls.super_nes_console, cls.psx_console],
            release_date=datetime.date(1995, 3, 11),
            publisher_of_game=cls.square_publisher,
            players_that_own_game=[],
            tags_for_game=[cls.rpg_tag, cls.turn_based_tag, cls.two_dimensional_tag],
        )

        cls.resident_evil_game = GameFactory(
            title="Resident Evil 2",
            game_consoles_released_on=[
                cls.dc_console,
                cls.psx_console,
                cls.windows_console,
            ],
            release_date=datetime.date(1998, 1, 21),
            publisher_of_game=cls.capcom_publisher,
            players_that_own_game=[],
            tags_for_game=[cls.action_tag, cls.three_dimensional_tag],
        )

        cls.doom_game = GameFactory(
            title="DOOM",
            game_consoles_released_on=[
                cls.super_nes_console,
                cls.psx_console,
                cls.windows_console,
            ],
            release_date=datetime.date(1993, 12, 10),
            publisher_of_game=cls.Id_software_publisher,
            players_that_own_game=[],
            tags_for_game=[
                cls.action_tag,
                cls.three_dimensional_tag,
                cls.shooter_tag,
                cls.fps_tag,
            ],
        )

        cls.quake_game = GameFactory(
            title="Quake 3 Arena",
            game_consoles_released_on=[cls.dc_console, cls.windows_console],
            release_date=datetime.date(1999, 12, 2),
            publisher_of_game=cls.Id_software_publisher,
            players_that_own_game=[],
            tags_for_game=[
                cls.action_tag,
                cls.three_dimensional_tag,
                cls.shooter_tag,
                cls.fps_tag,
                cls.multi_player_tag,
            ],
        )

    def convert_ordered_dict_to_list(self, arr_of_ordered_dicts):
        return [
            json.loads(json.dumps(ordered_dicts))
            for ordered_dicts in arr_of_ordered_dicts
        ]

    def test_get_games_based_on_query_parameters(self):
        query_params_fft = {
            "tags": ",".join([self.strategy_tag.name, self.rpg_tag.name]),
            "publisher": self.square_publisher.name,
            "consoles": self.psx_console.name_code,
        }
        response_from_get_fft = self.client.get(GET_GAME_URL, query_params_fft)
        game_found_from_query_fft = self.convert_ordered_dict_to_list(
            response_from_get_fft.data
        )
        self.assertEqual(response_from_get_fft.status_code, status.HTTP_200_OK)
        self.assertEqual(len(game_found_from_query_fft), 1)
        self.assertEqual(
            game_found_from_query_fft[0]["title"], self.final_fantasy_game.title
        )

    def test_get_games_based_on_tags(self):
        query_params_fps = {"tags": self.fps_tag.name}
        response_from_get_fps_games = self.client.get(GET_GAME_URL, query_params_fps)
        games_found_from_fps_query = self.convert_ordered_dict_to_list(
            response_from_get_fps_games.data
        )
        titles_of_games_found_in_fps_query = sorted(
            [obj["title"] for obj in games_found_from_fps_query]
        )
        expected_titles_from_fps_query = sorted(
            [self.doom_game.title, self.quake_game.title]
        )
        self.assertEqual(response_from_get_fps_games.status_code, status.HTTP_200_OK)
        self.assertEqual(len(games_found_from_fps_query), 2)
        self.assertEqual(
            titles_of_games_found_in_fps_query, expected_titles_from_fps_query
        )

        query_params_2d_action = {
            "tags": ",".join([self.action_tag.name, self.two_dimensional_tag.name])
        }
        response_from_2d_action_query = self.client.get(
            GET_GAME_URL, query_params_2d_action
        )
        games_found_from_2d_action_query = self.convert_ordered_dict_to_list(
            response_from_2d_action_query.data
        )
        titles_found_from_2d_action_query = sorted(
            [obj["title"] for obj in games_found_from_2d_action_query]
        )
        titles_of_games_expected_in_2d_action_query = sorted(
            [
                self.megaman_game.title,
                self.castlevania_game.title,
                self.contra_game.title,
                self.ghouls_ghost_game.title,
            ]
        )
        self.assertEqual(response_from_2d_action_query.status_code, status.HTTP_200_OK)
        self.assertEqual(len(games_found_from_2d_action_query), 4)
        self.assertEqual(
            titles_found_from_2d_action_query,
            titles_of_games_expected_in_2d_action_query,
        )

        query_params_general_shooter = {"tags": self.shooter_tag.name}
        response_from_shooter_query = self.client.get(
            GET_GAME_URL, query_params_general_shooter
        )
        games_found_from_shooter_query = self.convert_ordered_dict_to_list(
            response_from_shooter_query.data
        )
        titles_found_in_fps_query = sorted(
            [obj["title"] for obj in games_found_from_shooter_query]
        )
        titles_of_games_expected_in_shooter_query = sorted(
            [self.contra_game.title, self.doom_game.title, self.quake_game.title]
        )
        self.assertEqual(response_from_2d_action_query.status_code, status.HTTP_200_OK)
        self.assertEqual(
            titles_found_in_fps_query, titles_of_games_expected_in_shooter_query
        )
        self.assertEqual(len(games_found_from_shooter_query), 3)

    def get_games_based_on_publisher_and_console(self):
        query_params_16bit_capcom = {
            "publisher": self.capcom_publisher,
            "consoles": ",".join(
                [self.super_nes_console.name_code, self.genesis_console.name_code]
            ),
        }
        response_from_get_16bit_capcom = self.client.get(
            GET_GAME_URL, query_params_16bit_capcom
        )
        games_found_from_16bit_capcom_query = response_from_get_16bit_capcom.data
        title_of_games_found_in_16bit_capcom_query = sorted(
            [obj.title for obj in games_found_from_16bit_capcom_query]
        )
        expected_titles_from_16bit_capcom_query = sorted(
            [self.ghouls_ghost_game.title, self.megaman_game.title]
        )
        self.assertEqual(response_from_get_16bit_capcom.status_code, status.HTTP_200_OK)
        self.assertEqual(len(games_found_from_16bit_capcom_query), 2)
        self.assertEqual(
            title_of_games_found_in_16bit_capcom_query,
            expected_titles_from_16bit_capcom_query,
        )

    def get_games_based_on_tag_and_console(self):
        query_params_3d_games_on_psx_and_dc = {
            "tags": self.three_dimensional_tag.name,
            "consoles": ",".join(
                [self.psx_console.name_code, self.dc_console.name_code]
            ),
        }
        response_from_get_3d_psx_dc = self.client.get(
            GET_GAME_URL, query_params_3d_games_on_psx_and_dc
        )
        games_found_from_3d_psx_dc_query = sorted(
            [obj.title for obj in response_from_get_3d_psx_dc.data]
        )
        expected_titles_from_3d_psx_dc_query = sorted(
            [
                self.resident_evil_game.title,
                self.quake_game.title,
                self.doom_game.title,
                self.final_fantasy_game.title,
            ]
        )
        self.assertEqual(response_from_get_3d_psx_dc.status_code, status.HTTP_200_OK)
        self.assertEqual(len(games_found_from_3d_psx_dc_query), 4)
        self.assertEqual(
            games_found_from_3d_psx_dc_query, expected_titles_from_3d_psx_dc_query
        )


class TestsForPrivateGameCollectionApi(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Tags for games"""
        cls.action_tag = TagFactory(name="action")
        cls.platformer_tag = TagFactory(name="platformer")

        cls.single_player_tag = TagFactory(name="single-player")
        cls.multi_player_tag = TagFactory(name="multi-player")

        cls.rpg_tag = TagFactory(name="rpg")
        cls.strategy_tag = TagFactory(name="strategy")
        cls.turn_based_tag = TagFactory(name="turn-based")

        cls.shooter_tag = TagFactory(name="shooter")
        cls.fps_tag = TagFactory(name="first person shooter")

        cls.two_dimensional_tag = TagFactory(name="2d")
        cls.three_dimensional_tag = TagFactory(name="3d")

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
        cls.windows_console = GameConsoleFactory(
            name="Windows", maker_of_console=cls.microsoft_brand, name_code="WIN"
        )

        """Video game publishers"""
        cls.sega_publisher = PublisherFactory(name="sega")
        cls.square_publisher = PublisherFactory(name="square-enix")
        cls.Id_software_publisher = PublisherFactory(name="id-software")

        cls.final_fantasy_game = GameFactory(
            title="Final Fantasy Tactics",
            game_consoles_released_on=[cls.psx_console],
            release_date=datetime.date(1997, 6, 20),
            publisher_of_game=cls.square_publisher,
            players_that_own_game=[],
            tags_for_game=[
                cls.rpg_tag,
                cls.turn_based_tag,
                cls.strategy_tag,
                cls.three_dimensional_tag,
            ],
        )

        cls.shining_force_game = GameFactory(
            title="Shining Force",
            game_consoles_released_on=[cls.genesis_console],
            release_date=datetime.date(1992, 3, 20),
            publisher_of_game=cls.sega_publisher,
            players_that_own_game=[],
            tags_for_game=[
                cls.rpg_tag,
                cls.turn_based_tag,
                cls.strategy_tag,
                cls.three_dimensional_tag,
            ],
        )

        cls.doom_game = GameFactory(
            title="DOOM",
            game_consoles_released_on=[
                cls.super_nes_console,
                cls.psx_console,
                cls.windows_console,
            ],
            release_date=datetime.date(1993, 12, 10),
            publisher_of_game=cls.Id_software_publisher,
            players_that_own_game=[],
            tags_for_game=[
                cls.action_tag,
                cls.three_dimensional_tag,
                cls.shooter_tag,
                cls.fps_tag,
            ],
        )

        cls.chrono_trigger_game = GameFactory(
            title="Chrono Trigger",
            game_consoles_released_on=[cls.super_nes_console, cls.psx_console],
            release_date=datetime.date(1995, 3, 11),
            publisher_of_game=cls.square_publisher,
            players_that_own_game=[],
            tags_for_game=[cls.rpg_tag, cls.turn_based_tag, cls.two_dimensional_tag],
        )

    def convert_ordered_dict_to_list(self, arr_of_ordered_dicts):
        return [
            json.loads(json.dumps(ordered_dicts))
            for ordered_dicts in arr_of_ordered_dicts
        ]

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "rpg_fan_420@blazeit.com", "gaming_is_AWESOME#!@#@#331"
        )
        self.client.force_authenticate(self.user)

    def test_add_game_to_users_collection(self):
        """Test if user can add a game to their collection"""
        finaly_fantasy_obj = Game.objects.get(title=self.final_fantasy_game.title)

        payload = {"game_id": finaly_fantasy_obj.id}

        response_from_add_game_to_collection = self.client.put(
            ADD_TO_COLLECTION_URL, payload
        )
        self.assertEqual(
            response_from_add_game_to_collection.status_code, status.HTTP_200_OK
        )

        response_from_get_user_collection = self.client.get(GET_COLLECTION_URL)
        self.assertEqual(
            response_from_add_game_to_collection.status_code, status.HTTP_200_OK
        )
        games_found_in_query = self.convert_ordered_dict_to_list(
            response_from_get_user_collection.data
        )
        title_of_games_in_users_collection = [
            obj["title"] for obj in games_found_in_query
        ]
        expected_result_from_get_collection_query = [finaly_fantasy_obj.title]
        self.assertEqual(
            title_of_games_in_users_collection,
            expected_result_from_get_collection_query,
        )

    def test_remove_game_from_users_collection(self):
        """Test if user can remove game from their collection"""
        ids_of_games_to_add = [
            self.final_fantasy_game.id,
            self.shining_force_game.id,
            self.chrono_trigger_game.id,
        ]

        for game_id in ids_of_games_to_add:
            response_from_adding_game = self.client.put(
                ADD_TO_COLLECTION_URL, {"game_id": game_id}
            )
            self.assertEqual(response_from_adding_game.status_code, status.HTTP_200_OK)

        response_from_removing_game = self.client.put(
            REMOVE_FROM_COLLECTION_URL, {"game_id": self.shining_force_game.id}
        )
        self.assertEqual(response_from_removing_game.status_code, status.HTTP_200_OK)

        response_from_get_user_collection = self.client.get(GET_COLLECTION_URL)
        self.assertEqual(
            response_from_get_user_collection.status_code, status.HTTP_200_OK
        )
        games_found_in_query = self.convert_ordered_dict_to_list(
            response_from_get_user_collection.data
        )
        ids_of_games_in_users_collection = sorted(
            [obj["title"] for obj in games_found_in_query]
        )
        expected_result_from_get_collection_query = sorted(
            [self.final_fantasy_game.title, self.chrono_trigger_game.title]
        )
        self.assertEqual(
            ids_of_games_in_users_collection, expected_result_from_get_collection_query
        )

    def test_game_collection_matches_authenticated_users(self):
        """Test if authenticated user can only add games to their own collection, and not other users, And vice-versa"""

        fps_nerds_email = "fps_nerd_420@pwnnoobs.com"
        fps_nerd = get_user_model().objects.create_user(
            email=fps_nerds_email, password="gaming_is_AMAAAAAZING#!@#@#551"
        )

        doom_obj = Game.objects.get(id=self.doom_game.id)
        fps_nerd.games_owned_by_player.add(doom_obj)

        response_from_authenticated_user_adding_to_their_collection = self.client.put(
            ADD_TO_COLLECTION_URL, {"game_id": self.shining_force_game.id}
        )
        self.assertEqual(
            response_from_authenticated_user_adding_to_their_collection.status_code,
            status.HTTP_200_OK,
        )

        fps_nerds_game_collection = list(
            get_user_model()
            .objects.get(id=fps_nerd.id)
            .games_owned_by_player.all()
            .values()
            .distinct()
        )
        ids_of_games_in_fps_nerds_collection = sorted(
            [obj["id"] for obj in fps_nerds_game_collection]
        )
        self.assertNotIn(
            self.shining_force_game.id, ids_of_games_in_fps_nerds_collection
        )
