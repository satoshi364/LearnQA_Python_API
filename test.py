import requests


def test_homework_cookie():
    url = "https://playground.learnqa.ru/api/homework_cookie"
    response = requests.get(url)
    print(response.cookies)

    cookie_name = "HomeWork"
    expected_cookie_value = "hw_value"

    assert cookie_name in response.cookies, f"Expected cookie {cookie_name} not found"
    assert response.cookies[
               cookie_name] == expected_cookie_value, f"Unexpected value for cookie {cookie_name}: {response.cookies[cookie_name]}"
