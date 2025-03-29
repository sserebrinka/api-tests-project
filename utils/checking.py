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

    """Метод для проверки значений обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, "Значение поля не совпадает с ожидаемым"
        print(f"Значение поля {field_name} верно!")