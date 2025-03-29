import requests
import json

"""Методы для проверки ответов запросов"""

class Checking():

    """Метод для проверки статус-кода"""
    @staticmethod
    def check_status_code(response, status_code):
        assert status_code == response.status_code, f"Ожидался статус {status_code}, получен {response.status_code}"
        print(f"Успешно! Статус-код: {str(response.status_code)}")

    """Метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(response, expected_tokens):
        tokens = list(json.loads(response.text))
        assert tokens == expected_tokens, f"Отсутствуют ключи: {set(expected_tokens) - set(tokens)}"
        print("Все обязательные поля присутствуют")
