from operator import truediv
from flask import Flask,request,send_file,jsonify


def send_text_msg(robwxid, to_wxid, msg):#发送文字
    data = dict()
    data['success'] = True  # Api数值（可以参考 - api列表demo）
    data['message'] = 'successful!' # 发送内容
    data['event'] = "SendTextMsg"  # api
    data['to_wxid'] = to_wxid  # 对方id
    data['robot_wxid'] = robwxid  # 账户id，用哪个账号去发送这条消息
    data["msg"] = msg
    return data


def send_image_msg(robwxid, to_wxid, image):#发送图片
    print("fasongtupian")
    data = dict()
    data['success'] = True  # Api数值（可以参考 - api列表demo）
    data['message'] = 'successful!' # 发送内容
    data['event'] = "SendImageMsg"  # api
    data['to_wxid'] = to_wxid  # 对方id
    data['robot_wxid'] = robwxid  # 账户id，用哪个账号去发送这条消息
    data["msg"] = image
    return data



