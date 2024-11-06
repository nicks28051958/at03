import pytest
import requests
from cat_api import get_random_cat_image


# Тест успешного запроса
def test_get_random_cat_image_success(requests_mock):
    url = "https://api.thecatapi.com/v1/images/search"
    # Мокаем успешный ответ с изображением
    requests_mock.get(url, json=[{"url": "https://example.com/cat.jpg"}], status_code=200)

    result = get_random_cat_image()
    assert result == "https://example.com/cat.jpg", "Должно вернуть правильный URL изображения кошки"


# Тест неуспешного запроса
def test_get_random_cat_image_failure(requests_mock):
    url = "https://api.thecatapi.com/v1/images/search"
    # Мокаем неуспешный запрос с кодом 404
    requests_mock.get(url, status_code=404)

    result = get_random_cat_image()
    assert result is None, "Должно вернуть None при ошибочном статусе запроса"
