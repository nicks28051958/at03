import requests

def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        # Проверка успешного запроса
        if response.status_code == 200:
            data = response.json()
            # Проверка, что в ответе есть данные и ключ 'url'
            if data and 'url' in data[0]:
                return data[0]['url']
        return None
    except requests.RequestException:
        # Вернем None при ошибке запроса
        return None

# Пример использования
print(get_random_cat_image())
