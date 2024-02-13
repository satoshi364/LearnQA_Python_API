import requests
import pytest

def test_homework_header():
    response = requests.get("https://playground.learnqa.ru/api/homework_header")
    headers = response.headers
    print("Headers:", headers)

    expected_values = {
        'Date': 'Tue, 13 Feb 2024 18:01:19 GMT',
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Length': '0',
        'Connection': 'keep-alive',
        'Keep-Alive': 'timeout=10',
        'Server': 'Apache',
        'Set-Cookie': 'HomeWork=hw_value; expires=Fri, 15-Mar-2024 18:01:19 GMT; Max-Age=2678400; path=/; domain=playground.learnqa.ru; HttpOnly',
        'Cache-Control': 'max-age=0',
        'Expires': 'Tue, 13 Feb 2024 18:01:19 GMT'
    }

    for header, expected_value in expected_values.items():
        assert headers.get(header) == expected_value, f"Unexpected value for header {header}: {headers.get(header)}"