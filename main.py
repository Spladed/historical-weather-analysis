import time
import requests

def get_all_history_data(currentYear, currentMonth, city):
    print(f'Hi, {city}')

def get_furthest_time():
    return 2011


if __name__ == '__main__':
    localTime = time.localtime(time.time())
    currentYear = time.strftime("%Y", localTime)
    currentMonth = time.strftime("%m", localTime)
    city = "wuzhong"
    get_all_history_data(currentYear, currentMonth, city)