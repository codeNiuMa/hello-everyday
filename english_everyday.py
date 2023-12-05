# encoding:utf-8

import requests as re
from datetime import datetime

today = datetime.today().date()  # 2023-12-05
# print(today)

response = re.get(f'http://sentence.iciba.com/index.php?c=dailysentence&m=getdetail&title={today}').json()
# print(response)

en = response['content']
zh = response['note']
# print(en, zh)
