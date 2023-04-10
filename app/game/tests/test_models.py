from django.test import TestCase
from game.models import Game
import datetime
from django.contrib.auth import get_user_model
from tag.tests.factories import TagFactory
from gameconsole.tests.factories import GameConsoleFactory
from consolemaker.tests.factories import ConsoleMakerFactory
from publisher.tests.factories import PublisherFactory
from game.tests.factories import GameFactory

class GameTests(TestCase):
    """Test module for Game model"""

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
        
        cls.two_dimensional_tag =TagFactory(name="2d")
        cls.three_dimensional_tag = TagFactory(name="3d")

        """Brands for console manfucaturers"""
        cls.nintendo_brand = ConsoleMakerFactory(name="nintendo")
        cls.sega_brand = ConsoleMakerFactory(name='sega')
        cls.sony_brand = ConsoleMakerFactory(name='sony')
        cls.microsoft_brand = ConsoleMakerFactory(name='microsoft')

        """Video game consoles"""
        cls.genesis_console = GameConsoleFactory(name="Genesis", maker_of_console=cls.sega_brand, name_code="MD")
        cls.super_nes_console =GameConsoleFactory(name="Super Nintendo", maker_of_console=cls.nintendo_brand, name_code="SNES")
        cls.psx_console = GameConsoleFactory(name="Playstation", maker_of_console=cls.sony_brand, name_code="PSX")
        cls.dc_console = GameConsoleFactory(name="Dreamcast", maker_of_console=cls.sega_brand, name_code="DC")
        cls.windows_console = GameConsoleFactory(name="Windows", maker_of_console=cls.microsoft_brand, name_code="WIN")

        """Video game publishers"""
        cls.capcom_publisher = PublisherFactory(name='capcom')
        cls.konami_publisher = PublisherFactory(name='konami')
        cls.sega_publisher = PublisherFactory(name='sega')
        cls.square_publisher = PublisherFactory(name="square-enix")
        cls.Id_software_publisher = PublisherFactory(name='id-software')

        """Games (some of my actual favorite games ever)"""
        cls.castlevania_game = GameFactory(
            title="Super Castlevania 4",
            game_consoles_released_on=[cls.super_nes_console],
            release_date = datetime.date(1991, 12, 4),
            publisher_of_game = cls.konami_publisher,
            players_that_own_game = [],
            tags_for_game=[cls.action_tag, cls.platformer_tag, cls.two_dimensional_tag]
        )

        cls.megaman_game = GameFactory(
            title="Megaman X",
            game_consoles_released_on=[cls.super_nes_console],
            release_date = datetime.date(1993, 12, 17),
            publisher_of_game = cls.capcom_publisher,
            players_that_own_game = [],
            tags_for_game=[cls.action_tag, cls.platformer_tag, cls.two_dimensional_tag]
        )

        cls.ghouls_ghost_game = GameFactory(
            title="Ghouls 'n Ghosts",
            game_consoles_released_on=[cls.genesis_console],
            release_date = datetime.date(1989, 9, 17),
            publisher_of_game = cls.capcom_publisher,
            players_that_own_game = [],
            tags_for_game=[cls.action_tag, cls.platformer_tag, cls.two_dimensional_tag]
        )

        cls.contra_game = GameFactory(
            title="Contra: Hard Corps",
            game_consoles_released_on=[cls.genesis_console],
            release_date = datetime.date(1994, 8, 8),
            publisher_of_game = cls.konami_publisher,
            players_that_own_game = [],
            tags_for_game=[cls.action_tag, cls.platformer_tag, cls.two_dimensional_tag, cls.shooter_tag]
        )

        cls.final_fantasy_game = GameFactory(
            title="Final Fantasy Tactics",
            game_consoles_released_on=[cls.psx_console],
            release_date = datetime.date(1997, 6, 20),
            publisher_of_game = cls.square_publisher,
            players_that_own_game = [],
            tags_for_game=[cls.rpg_tag, cls.turn_based_tag, cls.strategy_tag, cls.three_dimensional_tag]
        )

        cls.shining_force_game = GameFactory(
            title="Shining Force",
            game_consoles_released_on=[cls.genesis_console],
            release_date = datetime.date(1992, 3, 20),
            publisher_of_game = cls.sega_publisher,
            players_that_own_game = [],
            tags_for_game=[cls.rpg_tag, cls.turn_based_tag, cls.strategy_tag, cls.three_dimensional_tag]
        )

        cls.chrono_trigger_game = GameFactory(
            title="Chrono Trigger",
            game_consoles_released_on=[cls.super_nes_console, cls.psx_console],
            release_date = datetime.date(1995, 3, 11),
            publisher_of_game = cls.square_publisher,
            players_that_own_game = [],
            tags_for_game=[cls.rpg_tag, cls.turn_based_tag, cls.two_dimensional_tag]
        )

        cls.resident_evil_game = GameFactory(
            title="Resident Evil 2",
            game_consoles_released_on=[cls.dc_console, cls.psx_console, cls.windows_console],
            release_date = datetime.date(1998, 1, 21),
            publisher_of_game = cls.capcom_publisher,
            players_that_own_game = [],
            tags_for_game=[cls.action_tag, cls.three_dimensional_tag]
        )

        cls.doom_game = GameFactory(
            title="DOOM",
            game_consoles_released_on=[cls.super_nes_console, cls.psx_console, cls.windows_console],
            release_date = datetime.date(1993, 12, 10),
            publisher_of_game = cls.Id_software_publisher,
            players_that_own_game = [],
            tags_for_game=[cls.action_tag, cls.three_dimensional_tag, cls.shooter_tag, cls.fps_tag]
        )

        cls.quake_game = GameFactory(
            title="Quake 3 Arena",
            game_consoles_released_on=[cls.dc_console, cls.windows_console],
            release_date = datetime.date(1999, 12, 2),
            publisher_of_game = cls.Id_software_publisher,
            players_that_own_game = [],
            tags_for_game=[cls.action_tag, cls.three_dimensional_tag, cls.shooter_tag, cls.fps_tag, cls.multi_player_tag]
        )

    def test_create_game(self):
        """"Test if can successfully create game for database"""
        
        new_game_title = "Power Stone 2"
        new_game = Game.objects.create(
            title= new_game_title,
            release_date = datetime.date(2000, 8, 23),
            publisher_of_game = self.capcom_publisher,
        )
        new_game.game_consoles_released_on.set([self.dc_console])
        new_game.tags_for_game.set([self.action_tag, self.three_dimensional_tag, self.multi_player_tag])
        new_game.players_that_own_game.set([])

        self.assertEqual(new_game.title, new_game_title)

        games_that_are_3d_and_multiplayer = list(Game.objects.filter(tags_for_game__in=[self.multi_player_tag]).filter(tags_for_game__in=[self.three_dimensional_tag]).values())
        self.assertEqual(2, len(games_that_are_3d_and_multiplayer))

        expected_games_from_3d_multiplayer_query = sorted([self.quake_game.title, new_game_title])
        actual_games_from_3d_multiplayer_query = sorted([obj['title'] for obj in games_that_are_3d_and_multiplayer])
        self.assertEqual(expected_games_from_3d_multiplayer_query, actual_games_from_3d_multiplayer_query)
    
    def test_update_game_info(self):
        """Update Game in database"""

        new_game_title = "Megaman Legends"

        new_game = Game.objects.create(
            title= new_game_title,
            release_date = datetime.date(1997, 12, 18),
            publisher_of_game = self.konami_publisher,
        )

        new_game.game_consoles_released_on.set([self.psx_console])
        new_game.tags_for_game.set([self.action_tag, self.three_dimensional_tag])
        new_game.players_that_own_game.set([])
        self.assertEqual(new_game.title, new_game_title)

        # Some information we entered is incorrect, missing so lets fix that.
        Game.objects.filter(title=new_game_title).update(publisher_of_game=self.capcom_publisher)
        game_obj_to_modify = Game.objects.get(title=new_game_title)
        game_obj_to_modify.game_consoles_released_on.set([self.psx_console, self.windows_console])

        # Check if the update we did works 
        updated_entry = Game.objects.get(title=new_game_title)
        number_of_consoles_for_updated_entry = len(list(updated_entry.game_consoles_released_on.all()))
        self.assertEqual(updated_entry.publisher_of_game, self.capcom_publisher)
        self.assertEqual(2, number_of_consoles_for_updated_entry)

    def test_get_games_for_specified_consoles(self):
        """Test if able to retrieve games for specified consoles"""
        
        resident_evil_obj = Game.objects.get(title=self.resident_evil_game.title)
        quake_obj = Game.objects.get(title=self.quake_game.title)
        doom_obj = Game.objects.get(title=self.doom_game.title)
        final_fantasy_obj = Game.objects.get(title=self.final_fantasy_game.title)
        chrono_trigger_obj = Game.objects.get(title=self.chrono_trigger_game.title)

        games_on_dreamcast = list(Game.objects.filter(game_consoles_released_on__in=[self.dc_console]).values())
        expected_result_dc = sorted([resident_evil_obj.title, quake_obj.title])
        actual_result_dc = sorted([obj['title'] for obj in games_on_dreamcast])

        self.assertEqual(expected_result_dc, actual_result_dc)
        self.assertEqual(2, len(actual_result_dc))

        #get games that were both released on Windows AND PSX. The games must have been released on both platforms
        games_on_both_psx_and_windows = list(Game.objects.filter(game_consoles_released_on__in=[self.windows_console]).filter(game_consoles_released_on__in=[self.psx_console]).values())
        expected_result_both_psx_windows = sorted([resident_evil_obj.title, doom_obj.title])
        actual_result_both_psx_windows = sorted([obj['title'] for obj in games_on_both_psx_and_windows])

        self.assertEqual(expected_result_both_psx_windows, actual_result_both_psx_windows)
        self.assertEqual(2, len(actual_result_both_psx_windows))

        #get games that were released on alteast one of the platforms in the query.
        games_on_psx_OR_windows = list(Game.objects.filter(game_consoles_released_on__in=[self.psx_console, self.windows_console]).values().distinct())
        expected_result_psx_OR_windows = sorted([final_fantasy_obj.title, chrono_trigger_obj.title, doom_obj.title, quake_obj.title, resident_evil_obj.title])
        actual_result_psx_OR_windows = sorted([obj['title'] for obj in games_on_psx_OR_windows])

        self.assertEqual(5, len(actual_result_psx_OR_windows))
        self.assertEqual(actual_result_psx_OR_windows, expected_result_psx_OR_windows)


    def test_get_games_from_specified_publisher(self):
        """Retrieve games from specified publisher"""

        castlevania_obj = Game.objects.get(title=self.castlevania_game.title)
        megaman_obj = Game.objects.get(title=self.megaman_game.title)
        ghouls_ghosts_obj = Game.objects.get(title=self.ghouls_ghost_game.title)
        contra_obj = Game.objects.get(title=self.contra_game.title)
        resident_evil_obj = Game.objects.get(title=self.resident_evil_game.title)

        games_published_by_capcom = list(Game.objects.filter(publisher_of_game=self.capcom_publisher).values())
        expected_result_capcom_games_query = sorted([megaman_obj.title, ghouls_ghosts_obj.title, resident_evil_obj.title])
        actual_result_capcom_games_query = sorted([obj['title'] for obj in games_published_by_capcom])

        self.assertEqual(expected_result_capcom_games_query, actual_result_capcom_games_query)
        self.assertEqual(3, len(actual_result_capcom_games_query))

        konami_games_released_on_genesis = list(Game.objects.filter(publisher_of_game=self.konami_publisher, game_consoles_released_on__in=[self.genesis_console]).values())
        expect_result_konami_sega_query = [contra_obj.title]
        unexpected_result_konami_sega_query = sorted([castlevania_obj.title, contra_obj.title])
        actual_result_konami_sega_query = sorted([obj['title'] for obj in konami_games_released_on_genesis])

        self.assertEqual(expect_result_konami_sega_query, actual_result_konami_sega_query)
        self.assertEqual(1, len(konami_games_released_on_genesis))
        self.assertNotEqual(unexpected_result_konami_sega_query, actual_result_konami_sega_query)
        
    def test_get_list_of_games_based_on_tags(self):
        """Test for querying for games based on a number of combination  of tags"""

        #I want any game that falls under the general RPG category
        final_fantasy_obj = Game.objects.get(title=self.final_fantasy_game.title)
        shining_force_obj = Game.objects.get(title=self.shining_force_game.title)
        chrono_trigger_obj = Game.objects.get(title=self.chrono_trigger_game.title)

        games_under_general_rpg_category = list(Game.objects.filter(tags_for_game__in=[self.rpg_tag]).values())
        expected_result_general_rpgs = sorted([final_fantasy_obj.title, shining_force_obj.title, chrono_trigger_obj.title])
        actual_result_general_rpgs = sorted([obj['title'] for obj in games_under_general_rpg_category])

        self.assertEqual(actual_result_general_rpgs, expected_result_general_rpgs)
        self.assertEqual(3, len(actual_result_general_rpgs))

        #I want RPG games, but strictly ones that fall under the strategy-rpg sub-genre
        games_under_strategy_subcategory = list(Game.objects.filter(tags_for_game__in=[self.rpg_tag]).filter(tags_for_game__in=[self.strategy_tag]).values())
        expected_result_strategy_rpg = sorted([final_fantasy_obj.title, shining_force_obj.title])
        unexpected_result_strategy_rpg = sorted([final_fantasy_obj.title, shining_force_obj.title, chrono_trigger_obj.title])
        actual_result_strategy_rpg = sorted([obj['title'] for obj in games_under_strategy_subcategory])

        self.assertEqual(2, len(actual_result_strategy_rpg))
        self.assertEqual(actual_result_strategy_rpg, expected_result_strategy_rpg)
        self.assertNotEqual(actual_result_strategy_rpg, unexpected_result_strategy_rpg)

        #I want any shooter games, be they 2d or 3d, so I should get Contra, Doom, and Quake in this query
        games_under_general_shooter_category = list(Game.objects.filter(tags_for_game__in=[self.shooter_tag]).values())
        
        doom_obj = Game.objects.get(title=self.doom_game.title)
        quake_obj = Game.objects.get(title=self.quake_game.title)
        contra_obj = Game.objects.get(title=self.contra_game.title)

        expected_result_general_shooter = sorted([doom_obj.title, quake_obj.title, contra_obj.title])
        actual_result_general_shooter = sorted([obj['title'] for obj in games_under_general_shooter_category])

        self.assertEqual(expected_result_general_shooter, actual_result_general_shooter)
        self.assertEqual(3, len(actual_result_general_shooter))

        #I want shooter games, but ones that fall under the first-person-shooter category, so that means no 2d ones like contra
        games_under_fps_subcategory = list(Game.objects.filter(tags_for_game__in=[self.shooter_tag]).filter(tags_for_game__in=[self.fps_tag]).values())

        expected_result_fps = sorted([doom_obj.title, quake_obj.title])
        unexpected_result_fps = sorted([doom_obj.title, quake_obj.title, contra_obj.title])
        actual_result_fps = sorted([obj['title'] for obj in games_under_fps_subcategory])

        self.assertEqual(expected_result_fps, actual_result_fps)
        self.assertNotEqual(unexpected_result_fps, actual_result_fps)
        self.assertEqual(2, len(actual_result_fps))

        #I want 2D actions games. There are four 2D-action games in this test suite. And there shouldn't be any 3D games listed in this query
        castlevania_obj = Game.objects.get(title=self.castlevania_game.title)
        megaman_obj = Game.objects.get(title=self.megaman_game.title)
        ghouls_ghosts_obj = Game.objects.get(title=self.ghouls_ghost_game.title)

        action_games_that_are_2d = list(Game.objects.filter(tags_for_game__in=[self.action_tag]).filter(tags_for_game__in=[self.two_dimensional_tag]).values())
        expected_result_2d_action = sorted([castlevania_obj.title, megaman_obj.title, ghouls_ghosts_obj.title, contra_obj.title])
        actual_result_2d_action = sorted([obj['title'] for obj in action_games_that_are_2d])

        self.assertEqual(4, len(action_games_that_are_2d))
        self.assertEqual(actual_result_2d_action, expected_result_2d_action)
    
    def test_adding_and_removing_games_to_players_collection(self):
        
        rpg_fan = get_user_model().objects.create_user(
            email="rpg_fan_69@testing.com",
            password="Testing123/!/"
        )

        final_fantasy_obj = Game.objects.get(title=self.final_fantasy_game.title)
        shining_force_obj = Game.objects.get(title=self.shining_force_game.title)
        chrono_trigger_obj = Game.objects.get(title=self.chrono_trigger_game.title)

        rpg_fan.games_owned_by_player.add(final_fantasy_obj)
        rpg_fan.games_owned_by_player.add(shining_force_obj)
        rpg_fan.games_owned_by_player.add(chrono_trigger_obj)

        rpg_fans_game_collection_after_adding_games = get_user_model().objects.get(email="rpg_fan_69@testing.com").games_owned_by_player.all()
        self.assertIn(final_fantasy_obj, rpg_fans_game_collection_after_adding_games)
        self.assertIn(shining_force_obj, rpg_fans_game_collection_after_adding_games)
        self.assertIn(chrono_trigger_obj, rpg_fans_game_collection_after_adding_games)

        rpg_fan.games_owned_by_player.remove(shining_force_obj)

        rpg_fans_game_collection_after_removing_games = get_user_model().objects.get(email="rpg_fan_69@testing.com").games_owned_by_player.all()
        self.assertIn(final_fantasy_obj, rpg_fans_game_collection_after_removing_games)
        self.assertNotIn(shining_force_obj, rpg_fans_game_collection_after_removing_games)
        self.assertIn(chrono_trigger_obj, rpg_fans_game_collection_after_removing_games)
