import requests
from lxml import etree
from catapi import *




def getxz(xz,robot_wxid,to_wxid,final_from_wxid):
    list=[]
    if xz == '天蝎座' :
        xz_text = 'tianxie'
    if xz == '白羊座' :
        xz_text = 'baiyang'
    if xz == '金牛座' :
        xz_text = 'jinniu'
    if xz == '双子座' :
        xz_text = 'shuangzi'
    if xz == '巨蟹座' :
        xz_text = 'juxie'
    if xz == '狮子座' :
        xz_text = 'shizi'
    if xz == '处女座' :
        xz_text = 'chunv'
    if xz == '天秤座' :
        xz_text = 'tiancheng'
    if xz == '射手座' :
        xz_text = 'sheshou'
    if xz == '摩羯座' :
        xz_text = 'mojie'
    if xz == '水瓶座' :
        xz_text = 'shuiping'
    if xz == '双鱼座' :
        xz_text = 'shuangyu'
    print(xz_text)

    html = requests.get('https://www.smxs.com/xingzuoriyun/' + xz_text  ).text
    y = etree.HTML(html)
    i=1
    
    while i<6:

        top1 = y.xpath('/html/body/div[4]/div[2]/div[2]/p['+ str(i) +']/text()')
        list.append(top1)
        i=i+1
    l1 = "".join(list[0])
    l2 = "".join(list[1])
    l3 = "".join(list[2])
    l4 = "".join(list[3])
    l5 = "".join(list[4])
    xzys = xz +'今日运势:\n' + '【综合运势】\n' + l1 + '\n' + '【爱情运势】\n' + l2+ '\n' + '【事业学业】\n' + l3+ '\n'+ '【财富运势】\n' + l4 + '\n'+ '【健康运势】\n' + l5 +'\n------------------------------------\n'
    re = send_text_msg(robot_wxid,to_wxid,xzys)

    return re


def getxw(robot_wxid,to_wxid,final_from_wxid):
    image = {
        'url': 'https://api.vvhan.com/api/60s',
        'name' : '60s.jpg'
    }
    re = send_image_msg(robot_wxid,to_wxid,image)
    return re
