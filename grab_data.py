import csv
import datetime
import os
import shutil
import time

import requests
from bs4 import BeautifulSoup

# 目标城市
city = "wuzhong"

# 数据存放目录
base_dir = "{}_data".format(city)

# 目标地址
url = 'http://lishi.tianqi.com/{city}/{date}.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36s'}

columns_name = ["日期", "最高气温", "最低气温", "天气", "风向"]


# 获取所有历史数据
def get_all_history_data(start_year):
    remove_dir(base_dir)
    mkdir(base_dir)
    local_time = time.localtime(time.time())
    current_year = int(time.strftime("%Y", local_time))
    current_month = int(time.strftime("%m", local_time))
    # 遍历年、月
    for year in range(start_year, current_year + 1):
        print("start to get data of year ", year)
        max_month = current_month + 1 if year == current_year else 13
        for month in range(1, max_month):
            date = datetime.date(year, month, 1).strftime("%Y%m")
            target_url = url.format(city=city, date=date)
            # 获取数据
            get_data(target_url, year, date)


def get_data(url, year, date):
    folder = "{}/{}".format(base_dir, year)
    mkdir(folder)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    li_list = [li.text for li in soup.select(".thrui > li")]
    with open("{}/{}.csv".format(folder, date), 'w') as f:
        writer = csv.writer(f)
        writer.writerow(columns_name)
        for li in li_list:
            data_array = [item.replace("℃", "").strip() for item in
                          list(filter(lambda val: len(val) != 0, li.split('\n')))]
            writer.writerow(data_array)


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        print("create dir: ", path)
        os.mkdir(path)


def remove_dir(path):
    folder = os.path.exists(path)
    if folder:
        print("reomve dir: ", path)
        shutil.rmtree(path)