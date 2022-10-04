# -*- coding:utf-8 -*-

from flask import Flask,request,send_file,jsonify
import requests
from catapi import *
from pokemon import *
import datetime 
from xz import *
from qiandao import *
from menu import *



app =Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return '<h2>机器人</h2>'

@app.route("/api",methods=['POST','GET'])
def hello_world():
    robid = 'wxid=wxid_pfiraxy3fq6622'
    if request.method == 'POST':
        wx_type = request.form.get("event")  # 数据类型
        msg = request.form.get("msg")  # 发送内容
        to_wxid = request.form.get("from_wxid")  # 1级来源id（比如发消息的人的id）
        from_name = request.form.get("from_name")  # 1级来源昵称（比如发消息的人昵称）
        final_from_wxid = request.form.get("final_from_wxid")  # 2级来源id（群消息事件下，1级来源为群id，2级来源为发消息的成员id，私聊事件下都一样）
        final_nickname = request.form.get("final_from_name")  # 2级来源昵称
        robot_wxid = request.form.get("robot_wxid")  # 当前登录的账号（机器人）标识id
        parameters = request.form.get("parameters")  # 附加参数（暂未用到，请忽略）
        ws_time = request.form.get("time")  # 请求时间(时间戳10位版本)



        print("api:",wx_type,"发信人1：",from_name,"发信人2：",final_nickname,"内容:",msg)
        print('消息来源id:',to_wxid)
        print('信息人微信id：',final_from_wxid)
        print('时间：',ws_time)
        print('机器人id：',robot_wxid)
        try:
            file_url = request.form.get("file_url")  # 如果是文件消息（图片、语音、视频、动态表情），这里则是可直接访问的网络地址，非文件消息时为空
        except:
            raise TypeError("请使用 http-api 2.4+以上的版本")


        if msg == '召唤修沟沟' or msg == '召唤修狗狗' or msg == '召唤修勾勾' or msg == '召唤小狗狗':
            print('发送菜单')
            menu(robot_wxid,to_wxid)
        





        if "签到" in msg :
            if robid in msg : #签到
                if to_wxid == "19943249599@chatroom":
                    getqd(robot_wxid,to_wxid,final_nickname,final_from_wxid)
                else:
                    send_text_msg(robot_wxid,to_wxid,'该群没有开通签到功能')

        

        if wx_type == "200": #群信息
            if robid in msg : #宝可梦
                if "注册宝可梦" in msg :
                    pokemon_login(robot_wxid,to_wxid,final_from_wxid)
                if "注册伊布" in msg :
                    pokmon_choose(robot_wxid,to_wxid,final_nickname,'133')
                if "注册小火龙" in msg :
                    pokmon_choose(robot_wxid,to_wxid,final_nickname,'4')
                if "注册妙蛙种子"  in msg :
                    pokmon_choose(robot_wxid,to_wxid,final_nickname,'1')
                if "注册杰尼龟" in msg :
                    pokmon_choose(robot_wxid,to_wxid,final_nickname,'7')



            if robid in msg : #星座
                if '白羊' in msg :
                    getxz('白羊座',robot_wxid,to_wxid,final_from_wxid)
                if '天蝎' in msg :
                    getxz('天蝎座',robot_wxid,to_wxid,final_from_wxid)
                if '金牛' in msg :
                    getxz('金牛座',robot_wxid,to_wxid,final_from_wxid)
                if '双子' in msg :
                    getxz('双子座',robot_wxid,to_wxid,final_from_wxid)
                if '巨蟹' in msg :
                    getxz('巨蟹座',robot_wxid,to_wxid,final_from_wxid)
                if '狮子' in msg :
                    getxz('狮子座',robot_wxid,to_wxid,final_from_wxid)
                if '处女' in msg :
                    getxz('处女座',robot_wxid,to_wxid,final_from_wxid)
                if '天秤' in msg :
                    getxz('天秤座',robot_wxid,to_wxid,final_from_wxid)
                if '射手' in msg :
                    getxz('射手座',robot_wxid,to_wxid,final_from_wxid)
                if '摩羯' in msg :
                    getxz('摩羯座',robot_wxid,to_wxid,final_from_wxid)
                if '水瓶' in msg :
                    getxz('水瓶座',robot_wxid,to_wxid,final_from_wxid)
                if '双鱼' in msg :
                    getxz('双鱼座',robot_wxid,to_wxid,final_from_wxid)           



    else:
        return f"GET访问测试页面，本机地址 http://192.168.226.1:5000/api" # 此处的测试地址应该是http://localhost:8074/复制到可爱猫功能-》HTTP多语言对-》消息回调地址
    return jsonify({"code": 200, "data": "result ok"})



if __name__ == "__main__":
    print('cs2')
    app.run(host="0.0.0.0",port=5000,debug=True)
