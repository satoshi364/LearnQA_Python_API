import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

response_1 = requests.get(url)
print("1. Запрос без параметра method:", response_1.text)

response_2 = requests.head(url)
print("2. Запрос не из списка (HEAD):", response_2.status_code)

valid_method = "POST"
params = {"method": valid_method}
response_3 = requests.post(url, data=params)
print(f"3. Запрос с правильным значением method ({valid_method}):", response_3.text)

print("4. Проверка всех возможных сочетаний:")
methods = ["GET", "POST", "PUT", "DELETE"]
for method in methods:
    for mismatch_method in methods:
        params = {"method": mismatch_method}
        if method == "GET":
            response = requests.get(url, params=params)
        else:
            response = requests.request(method, url, data=params)

        if response.status_code == 200:
            print(f"Совпадение! Тип запроса: {method}, Значение method: {mismatch_method}")
        else:
            print(f"Несовпадение. Тип запроса: {method}, Значение method: {mismatch_method}, Код ответа: {response.status_code}")