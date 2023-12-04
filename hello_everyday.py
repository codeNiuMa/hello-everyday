from datetime import datetime, timedelta

import Tools.scripts.highlight
import requests as re
from lxml import etree

from bug import english_everyday


def salary():
    # 今天过了15
    if today.day > 15:
        return datetime(today.year, today.month+1, 15)-today
    # 今天没有过15
    else:
        return 15-today.day
def bianli(list):
    if not list:
        # print('null_list')
        return 'null_list'

    if len(list) == 1:
        # print(list[0])
        return list[0]
    s = ''
    for i in list[:-1]:
        # print(i, end=',')
        s += i
        s += ','
    s += list[-1]
    return s

def news():
    r = re.get(
        'https://www.mxnzp.com/api/history/today?type=0&app_id=rgihdrm0kslojqvm&app_secret=WnhrK251TWlUUThqaVFWbG5OeGQwdz09')
    info = r.json()['data'][0]
    return (str(info['year'])+'-'+str(info['month'])+'-'+str(info['day'])+', '+info['title'])


head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
url = 'https://nongli.huashu-inc.com/'
result = re.get(url=url, headers=head).text
# print(result)
tree = etree.HTML(result)
list = tree.xpath('/html/body/div[2]/div[1]/div[1]/div[2]/table[2]/tr')

gongli = list[0].xpath('./td/text()')[0]  # 公元2023年12月3日 星期日
nongli = list[1].xpath('./td/text()')
nongli = nongli[0]+' '+nongli[1]  # 二零二三年 十月 廿一
ganzhi = str(list[2].xpath('./td/text()')[0]).split(' ')[0]  # 癸卯年
shengxiao = list[3].xpath('./td/a/text()')[0].replace('属','')
yi = list[11].xpath('./td[@colspan=\'2\']/text()') if not list[11].xpath('./td[@colspan=\'2\']/a/text()') else list[11].xpath('./td[@colspan=\'2\']/a/text()')
ji = list[12].xpath('./td[@colspan=\'2\']/text()') if not list[12].xpath('./td[@colspan=\'2\']/a/text()') else list[12].xpath('./td[@colspan=\'2\']/a/text()')
# print(ganzhi, shengxiao, yi, ji)

today = datetime.now()
s = \
f'''【摸鱼办】提醒您：{gongli.split(' ')[0]}，农历{ganzhi.replace('年', '')}[{shengxiao}]年{nongli.split(' ')[-2]+nongli.split(' ')[-1]}，{gongli.split(' ')[1]}，大家上午好，工作虽然辛苦，但也不要忘了休息，起来去茶水间、厕所或者走廊活动活动身体，祝愿所有打工人愉快地度过每一天...
【宜】 {bianli(yi)}
【忌】 {bianli(ji)}
距离【周末】还有{5-datetime.weekday(today)}天
距离【元旦】还有{(datetime(2024, 1, 1)-today).days+1}天
距离【春节】还有{(datetime(2024, 2, 10)-today).days+1}天
距离【周一】过去{datetime.weekday(today)+1-1}天({int(100*datetime.weekday(today)/6)}%)
距离【月初】过去{today.day}天({int(100*today.day/((datetime(today.year, today.month + 1, 1) - timedelta(days=1)).day  if today.month!=12 else 31))}%) 
距离【年初】过去{(today-datetime(today.year, 1, 1)).days}天({int((today-datetime(today.year, 1, 1)).days/3.65)}%)
距离【工资】还有{salary()}天
距离【退休】还有{(datetime(2050,1,1)-today).days}天(2050年50岁退休)
【每日英语】
{english_everyday.en}
{english_everyday.zh}
【每日一言】
{(re.get('https://v.api.aa1.cn/api/yiyan/index.php').text.removeprefix('<p>').removesuffix('</p>'))}
【历史上的今天】
{news()}
'''
print(s)
