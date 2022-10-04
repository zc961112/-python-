from catapi import *
import os
import time
from sql import *


path_py = os.path.abspath(__file__)#获取文件路径

def pokemon_login(robot_wxid,to_wxid,final_from_wxid):
    print("注册")
    try:
        with open(final_from_wxid,"r") as f :
            print("已存在")
        send_text_msg(robot_wxid,to_wxid,"已拥有账号")
    except:
        send_text_msg(robot_wxid,to_wxid,"请选择一只宝可梦作为你的第一个伙伴")
        send_text_msg(robot_wxid,to_wxid,"1-妙蛙种子")
        send_image_msg(robot_wxid,to_wxid,'E:\python项目\\flask微信机器人\wxbot\Pokemon\img\\1.jpg')
        time.sleep(2)
        send_text_msg(robot_wxid,to_wxid,"2-小火龙")
        send_image_msg(robot_wxid,to_wxid,'E:\python项目\\flask微信机器人\wxbot\Pokemon\img\\4.jpg')
        time.sleep(2)
        send_text_msg(robot_wxid,to_wxid,"3-杰尼龟")
        send_image_msg(robot_wxid,to_wxid,'E:\python项目\\flask微信机器人\wxbot\Pokemon\img\\7.jpg')
        time.sleep(2)
        send_text_msg(robot_wxid,to_wxid,"4-伊布")
        send_image_msg(robot_wxid,to_wxid,'E:\python项目\\flask微信机器人\wxbot\Pokemon\img\\133.jpg')
        time.sleep(2)
        send_text_msg(robot_wxid,to_wxid,"请输入伙伴名称（例如：注册伊布）")

def pokmon_choose(robot_wxid,to_wxid,final_nickname,num):
    path_py = os.path.abspath(__file__)#获取文件路径
    path = os.path.join(path_py,'..\Pokemon\\'+ 'login' +'\\' + final_nickname)
    if os.path.isfile(path):
        send_text_msg(robot_wxid,to_wxid,"已拥有账号")
    else:
        print('2')
        print("选择",num)
        location = 'B'+ str(int(num)+1)
        print(location)
        data_a=check_pokemon_excel('pokemon_info',location)
        print(data_a)
        send_text_msg(robot_wxid,to_wxid,"恭喜您获得伙伴："+ data_a)
        

