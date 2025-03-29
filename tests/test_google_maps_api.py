from utils.api import GoogleMapsApi
import requests

"""Создание, изменение и удаление новой локации"""
class TestCreatePlace():

    def test_create_new_place(self):

        print("\nМетод POST")
        result_post = GoogleMapsApi.create_new_place()

        # place_id
        check_post = result_post.json()
        place_id = check_post.get('place_id')

        print("\nМетод GET POST")
        result_get = GoogleMapsApi.get_new_place(place_id)

        print("\nМетод PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)

        print("\nМетод GET PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)

        print("\nМетод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)

        print("\nМетод GET DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)