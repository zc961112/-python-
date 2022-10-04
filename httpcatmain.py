# -*- coding:utf-8 -*-
from flask import Flask,request,send_file,jsonify
import requests
from catapi import *
from pokemon import *
from xz import *
from qiandao import *
from menu import *
import json

app =Flask(__name__)

@app.route('/',methods=['GET'])
def index():

    return '<h2>机器人</h2>'

@app.route("/api",methods=['POST','GET'])
def hello_world():
    robid = 'wxid=wxid_e9h9gif9r21w2'

    if request.method == 'POST':
        wx_type = request.json.get("event")  # 事件名称
        msg = request.json.get("msg")  # 发送内容
        to_wxid = request.json.get("from_wxid")  # 1级来源id（比如发消息的人的id）
        from_name = request.json.get("from_name")  # 1级来源昵称（比如发消息的人昵称）
        final_from_wxid = request.json.get("final_from_wxid")  # 2级来源id（群消息事件下，1级来源为群id，2级来源为发消息的成员id，私聊事件下都一样）
        final_nickname = request.json.get("final_from_name")  # 2级来源昵称
        robot_wxid = request.json.get("robot_wxid")  # 当前登录的账号（机器人）标识id
        type = request.json.get("type")  # 1/文本消息 3/图片消息 34/语音消息  42/名片消息  43/视频 47/动态表情 48/地理位置  49/分享链接  2000/转账 2001/红包  2002/小程序  2003/群邀请
        money = request.json.get('money') #money 金额，只有"EventReceivedTransfer"事件才有该参数

        print('------------------------------')
        print('事件名称：',wx_type)
        print('机器人id：',robot_wxid)
        print('内容类型',type)
        print('发信人',final_nickname)
        print('群id',to_wxid)
        print('群名',from_name)
        print('发信人id',final_from_wxid)        
        print('内容',msg)
        print('------------------------------')

        #菜单
        #=======================================================
        if msg == '召唤修沟沟' or msg == '召唤修狗狗' or msg == '召唤修勾勾' or msg == '召唤小狗狗':
            print('发送菜单')
            re = menu(robot_wxid,to_wxid)
            return jsonify(re)
        #=======================================================
        
        #签到
        #=======================================================
        if '签到' in msg :
            if robid in msg :
                if to_wxid == "47905053557@chatroom":
                    re = getqd(robot_wxid,to_wxid,final_nickname,final_from_wxid)
                    if '注册成功' in re :
                        re = getqd(robot_wxid,to_wxid,final_nickname,final_from_wxid)
                        return jsonify(re)
                    else:
                        return jsonify(re)

                else:
                    re = send_text_msg(robot_wxid,to_wxid,'该群没有开通签到功能')
                    return jsonify(re)
        #=======================================================

        if robid in msg :             
            #新闻
            #=======================================================
            if '新闻' in msg:
                re = getxw(robot_wxid,to_wxid,final_from_wxid)
                return jsonify(re)
            #星座
            #=======================================================
            if '白羊' in msg :
                re = getxz('白羊座',robot_wxid,to_wxid,final_from_wxid)
                return jsonify(re)
            if '天蝎' in msg :
                re = getxz('天蝎座',robot_wxid,to_wxid,final_from_wxid)
                return jsonify(re)
            if '金牛' in msg :
                re = getxz('金牛座',robot_wxid,to_wxid,final_from_wxid)
                return jsonify(re)
            if '双子' in msg :
                re = getxz('双子座',robot_wxid,to_wxid,final_from_wxid)
                return jsonify(re)
            if '巨蟹' in msg :
                re = getxz('巨蟹座',robot_wxid,to_wxid,final_from_wxid)
                return jsonify(re)
            if '狮子' in msg :
                re = getxz('狮子座',robot_wxid,to_wxid,final_from_wxid)
                return jsonify(re)
            if '处女' in msg :
                re = getxz('处女座',robot_wxid,to_wxid,final_from_wxid)
                return jsonify(re)
            if '天秤' in msg :
                re = getxz('天秤座',robot_wxid,to_wxid,final_from_wxid)
                return jsonify(re)
            if '射手' in msg :
                re = getxz('射手座',robot_wxid,to_wxid,final_from_wxid)
                return jsonify(re)
            if '摩羯' in msg :
                re = getxz('摩羯座',robot_wxid,to_wxid,final_from_wxid)
                return jsonify(re)
            if '水瓶' in msg :
                re = getxz('水瓶座',robot_wxid,to_wxid,final_from_wxid)
                return jsonify(re)
            if '双鱼' in msg :
                re = getxz('双鱼座',robot_wxid,to_wxid,final_from_wxid)
                return jsonify(re)
        #=======================================================
            
            if "注册宝可梦" in msg :
                re = pokemon_login(robot_wxid,to_wxid,final_from_wxid)
                return jsonify(re)
            if "注册伊布" in msg :
                re = pokmon_choose(robot_wxid,to_wxid,final_nickname,'133')
                return jsonify(re)
            if "注册小火龙" in msg :
                re = pokmon_choose(robot_wxid,to_wxid,final_nickname,'4')
                return jsonify(re)
            if "注册妙蛙种子"  in msg :
                re = pokmon_choose(robot_wxid,to_wxid,final_nickname,'1')
                return jsonify(re)
            if "注册杰尼龟" in msg :
                re = pokmon_choose(robot_wxid,to_wxid,final_nickname,'7')
                return jsonify(re)



        if  msg[:2] == '修勾' :
            msge = msg[2:]
            url = 'http://81.70.100.130/api/xiaoai.php?msg='+msge+'&n=text'
            html = requests.get(url).text
            re = send_text_msg(robot_wxid,to_wxid,html)
            return re



    else:
        return f"GET访问测试页面，本机地址 http://192.168.226.1:8000/api" 
    data = {"success": False, "message": "successful!", "event": "SendTextMsg", "to_wxid": "38767722387@chatroom", "robot_wxid": "wxid_pfiraxy3fq6622"}
    return jsonify(data)

    
if __name__ == "__main__":
    print('cs22')
    app.run(host="0.0.0.0",port=8000,debug=True)

