import requests
import time

def create_job():
    url = "https://playground.learnqa.ru/ajax/api/longtime_job"
    response = requests.get(url)
    return response.json()

def check_status_and_result(token):
    url = "https://playground.learnqa.ru/ajax/api/longtime_job"
    params = {"token": token}
    response = requests.get(url, params=params)
    return response.json()

print("1. Creating job")
job_info = create_job()
token = job_info["token"]
seconds_to_wait = job_info["seconds"]

status_before_waiting = check_status_and_result(token)["status"]
print(f"2. Status before waiting: {status_before_waiting}")

time.sleep(seconds_to_wait)

status_after_waiting = check_status_and_result(token)["status"]
result_after_waiting = check_status_and_result(token).get("result")

print(f"3. Status after waiting: {status_after_waiting}")
if result_after_waiting:
    print(f"4. Result after waiting: {result_after_waiting}")