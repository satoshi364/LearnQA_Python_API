import requests

url = "https://playground.learnqa.ru/api/long_redirect"
response = requests.get(url)

redirect_count = len(response.history)
print(f"Количество редиректов: {redirect_count}")

final_url = response.url
print(f"Итоговый URL: {final_url}")
