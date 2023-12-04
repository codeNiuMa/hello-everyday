# https://v.api.aa1.cn/api/yiyan/index.php
# app_id:rgihdrm0kslojqvmapp_secret:WnhrK251TWlUUThqaVFWbG5OeGQwdz09
import requests as re

cookies = {
    'update-95': '1',
    'update-1111': '1',
    'Hm_lvt_6188d53492b3951c5aa16a77f0b0e858': '1701223749,1701530240,1701616368,1701653110',
    'XSRF-TOKEN': 'eyJpdiI6IkVERzE2clgxZUE4Mnl0cWNRTml1WkE9PSIsInZhbHVlIjoiSUlsUVVZN2VIc2FqRG1TSTU1Q3pjOVpHR1JObmhDQXE2NTErWGU3Rm40cnVEd3dvZmNyWmIwY3FFRmt6NjRGdyIsIm1hYyI6IjZlYmE2MTdhMmFjOWIzMWVkZGI5YjhkZjliNjkyNTFhODZlYzYyODI3NDgzOGY3OTI2OTE1MGIxNTc4NzljNDAifQ%3D%3D',
    'laravel_session': 'eyJpdiI6InNMOGF1Y3hJeVYyZXMxa2lwQm16V0E9PSIsInZhbHVlIjoiTHRnR3FGd3l2M2NcL1NmU3FYeGoxVHl3TVUrbWVjUVN3b1JpM3NiYUxCcFZ6UWJuaGxHcklEVE4rcm5MZE1mc0kiLCJtYWMiOiI4NzAwYmY2MGUyZjVjYzRjNTUzMjQ2YzI1ZGRjNTM2YmM0OTU5NDdhZWU4ZDMxYmZjZTU5YTkzNjViZjZkZTMzIn0%3D',
    'Hm_lpvt_6188d53492b3951c5aa16a77f0b0e858': '1701655165',
}

headers = {
    'authority': 'www.free-api.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'update-95=1; update-1111=1; Hm_lvt_6188d53492b3951c5aa16a77f0b0e858=1701223749,1701530240,1701616368,1701653110; XSRF-TOKEN=eyJpdiI6IkVERzE2clgxZUE4Mnl0cWNRTml1WkE9PSIsInZhbHVlIjoiSUlsUVVZN2VIc2FqRG1TSTU1Q3pjOVpHR1JObmhDQXE2NTErWGU3Rm40cnVEd3dvZmNyWmIwY3FFRmt6NjRGdyIsIm1hYyI6IjZlYmE2MTdhMmFjOWIzMWVkZGI5YjhkZjliNjkyNTFhODZlYzYyODI3NDgzOGY3OTI2OTE1MGIxNTc4NzljNDAifQ%3D%3D; laravel_session=eyJpdiI6InNMOGF1Y3hJeVYyZXMxa2lwQm16V0E9PSIsInZhbHVlIjoiTHRnR3FGd3l2M2NcL1NmU3FYeGoxVHl3TVUrbWVjUVN3b1JpM3NiYUxCcFZ6UWJuaGxHcklEVE4rcm5MZE1mc0kiLCJtYWMiOiI4NzAwYmY2MGUyZjVjYzRjNTUzMjQ2YzI1ZGRjNTM2YmM0OTU5NDdhZWU4ZDMxYmZjZTU5YTkzNjViZjZkZTMzIn0%3D; Hm_lpvt_6188d53492b3951c5aa16a77f0b0e858=1701655165',
    'origin': 'https://www.free-api.com',
    'referer': 'https://www.free-api.com/use/626',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'x-csrf-token': 'UGnhqtMrgwQg0cmjxvG8fyzcGBsiTfiE6YWMEnys',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'fzsid': '626',
}

response = re.post('https://www.free-api.com/urltask', cookies=cookies, headers=headers, data=data).json()
en = response['msg']['result']['content']
zh = response['msg']['result']['note']

