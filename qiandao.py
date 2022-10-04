from re import L
from catapi import *
import os
import time
import pandas as pd
from pandas import DataFrame
import openpyxl



def getqd(robot_wxid,to_wxid,final_nickname,final_from_wxid):#机器人id，群id，用户名，用户id
    print('zhixing')
    text_true = '【'+ final_nickname+ '】' +"签到成功了哦,您的积分为【"
    text_flase = final_nickname + '！今天已经签到过啦！！！'
    text_none = '注册成功'
    path_py = os.path.abspath(__file__)#获取文件路径
    path = os.path.join(path_py,'..\签到\qd.xlsx')
    data = pd.read_excel(path,index_col='wxid')
    f = openpyxl.load_workbook(path)
    name = str(final_nickname)
    userid = str(final_from_wxid)
    day2 = time.strftime('%Y-%m-%d',time.localtime())
    print(userid)


    try:

        day1 = data.loc[userid,'签到日期']
        print('day1',day1)
        day1 = str(day1)[:10]
        if day1 == day2 :
            re = send_text_msg(robot_wxid,to_wxid,text_flase)

            return re
        else:
            print('321')
            user_point = int(data.loc[userid,'积分'])+1
            print(user_point)
            data.loc[userid,'积分'] = user_point
            data.loc[userid,'签到日期'] = day2

            DataFrame(data).to_excel(path)
            print('123')
            text = text_true + str(user_point) +'】'
            re = send_text_msg(robot_wxid,to_wxid,text)
            return re
    except:

        l = int(len(data))+2
        c_name = 'B' + str(l)
        c_uid = 'A' + str(l)
        c_point = 'C' +str(l)
        c_day = 'D' +str (l)
        table = f.active
        table[c_name] = name
        table[c_uid] = userid
        table[c_point] = 0
        table[c_day] = 1
        f.save(path)

        return text_none


        



