import requests

"""Методы для проверки ответов запросов"""

class Checking():

    """Метод для проверки статус-кода"""
    @staticmethod
    def check_status_code(response, status_code):
        assert status_code == response.status_code, "Статус-код не совпадает с ожидаемым"
        if response.status_code == status_code:
            print(f"Успешно! Статус-код: {str(response.status_code)}")
        else:
            print(f"Провал! Статус-код: {str(response.status_code)}")
