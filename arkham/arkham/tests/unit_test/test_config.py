
from unittest.mock import patch
from arkham.config import Settings
import pytest


class TestConfig:

    
    @pytest.fixture()
    def settingsObj(self):

        with patch("arkham.config.env"):
            with patch("arkham.config.eval"):

                settings = Settings("dfasga")
                return settings

    

    @patch("arkham.config.env")
    def test_pg_es_sync_return_true(self,patched_env,settingsObj):
        
        patched_env.get.return_value = "True"
        f = settingsObj.pg_es_sync
        
        patched_env.get.assert_called_once_with("PG_ES_SYNC")
        assert f == True
    
    # @patch("arkham.config.env")
    # @patch("arkham.config.jwt.decode")
    # @patch("arkham.config.Token")
    # @patch("arkham.config.time.time")
    # def test_get_s2s_token(self,patched_token,patched_jwt,patched_env,patched_time,settingsObj):

    #     patched_jwt.return_value = {"exp" : 2000}
    #     patched_time.return_value = 1000
    #     patched_token.get_token.return_value = "new_token"

    #     f = settingsObj.get_s2s_token
    #     assert  f == "new_token"





    
    def test_elastic_version(self,settingsObj):

        settingsObj._elastic_version = "v15"
        assert settingsObj.elastic_version == "v15"

    def test_elastic_major_version_for_None(self,settingsObj):

        settingsObj._elastic_version = None
        with pytest.raises(ValueError):
            settingsObj.elastic_major_version


    # @patch("arkham.config.Token")
    # def test_load_settings(self,patched_token,settingsObj):

    #     patched_token.get_token.return_value = "new_token"
    #     f = settingsObj.load_settings
    #     assert