from utils.api import GoogleMapsApi
from utils.checking import Checking
import requests
import allure
import json
from utils.logger import Logger

"""Создание, изменение и удаление новой локации"""
@allure.epic("Test create place")
class TestCreatePlace():

    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):
        print("\nМетод POST")
        result_post = GoogleMapsApi.create_new_place()
        Checking.check_status_code(result_post, 200)
        place_id = result_post.json().get("place_id")   # place_id
        token_post = self.get_list_token(result_post)
        Checking.check_json_token(result_post, token_post)
        Checking.check_json_value(result_post, 'status', 'OK')

        print("\nМетод GET POST")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        token_get = self.get_list_token(result_get)
        Checking.check_json_token(result_get, token_get)

        print("\nМетод PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        token_put = self.get_list_token(result_put)
        Checking.check_json_token(result_put, token_put)
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("\nМетод GET PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        token_get = self.get_list_token(result_get)
        Checking.check_json_token(result_get, token_get)

        print("\nМетод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        token_delete = self.get_list_token(result_delete)
        Checking.check_json_token(result_delete, token_delete)
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("\nМетод GET DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        token_get = self.get_list_token(result_get)
        Checking.check_json_token(result_get, token_get)
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")

        print("\nТестирование прошло успешно!")
    
    def get_list_token(self, response):
        return list(json.loads(response.text))
