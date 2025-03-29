from utils.http_methods import HttpMethods

"""Методы для тестирования Google Maps Api"""

BASE_URL = "https://rahulshettyacademy.com"    # базовый url
KEY = "?key=qaclick123"     # параметр для всех запросов

class GoogleMapsApi():

    """Метод для создания новой локации"""
    @staticmethod
    def create_new_place():
        
        json_for_create_new_place = { 
            "location": { 
                "lat": -38.383494, 
                "lng": 33.427362    
            }, "accuracy": 50, 
            "name": "Frontline house", 
            "phone_number": "(+91) 983 893 3937", 
            "address": "29, side layout, cohen 09", 
            "types": [
                "shoe park", 
                "shop"
            ],
            "website": "http://google.com", 
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"     # ресурс метода POST
        post_url = f"{BASE_URL}{post_resource}{KEY}"
        print(f"Запрос отправлен на url: {post_url}")

        result_post = HttpMethods.post(url=post_url, body=json_for_create_new_place)
        print(f"Результат POST запроса: {result_post.text}")

        return result_post
    
    """Метод для проверки новой локации"""

    @staticmethod
    def get_new_place(place_id):
        
        get_resource = "/maps/api/place/get/json"   # ресурс метода GET
        get_url = f"{BASE_URL}{get_resource}{KEY}&place_id={place_id}"
        print(f"Запрос отправлен на url: {get_url}")

        result_get = HttpMethods.get(url=get_url)
        print(f"Результат GET запроса: {result_get.text}")

        return result_get

    """Метод для изменения новой локации"""

    @staticmethod
    def put_new_place(place_id):

        put_resource = "/maps/api/place/update/json"
        put_url = f"{BASE_URL}{put_resource}{KEY}"

        json_for_update_new_location = {
            "place_id": place_id,
            "address":"101 Cheboksary, RU", 
            "key":"qaclick123" 
        }

        result_put = HttpMethods.put(url=put_url, body=json_for_update_new_location)
        print(f"Результат PUT запроса: {result_put.text}")

        return result_put
    
    """Метод для удаления новой локации"""

    @staticmethod
    def delete_new_place(place_id):

        delete_resource = "/maps/api/place/delete/json"
        delete_url = f"{BASE_URL}{delete_resource}{KEY}"

        json_for_delete_new_location = {
            "place_id": place_id
        }

        result_delete = HttpMethods.delete(url=delete_url, body=json_for_delete_new_location)
        print(f"Результат DELETE запроса: {result_delete.text}")

        return result_delete