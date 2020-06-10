#!/usr/bin/python
#coding:utf-8
'''
Created on 2020年1月25日

@author: HEWEI
'''

from threading import Timer
from wxpy import *

bot = None

def login_wechat():
    global bot
    #bot = Bot()
    bot = Bot(console_qr=2,cache_path="botoo.pkl")#linux环境上使用
    bot.enable_puid()

def send_notify():
    if bot == None:
        login_wechat()
    my_friend0 = bot.groups().search(u'正版融数')[0]
    my_friend0.send(u'大家好，我是本群的提醒打卡小助手，希望看到消息的人和我一起打一次卡。三小时后我继续提醒大家打卡。和我一起成为一天打八次卡的人吧！')
    my_friend1 = bot.groups().search(u'👉快乐平安—创新研发室👈')[0]
#     groups=my_friend1 = bot.groups()
#     for dd in groups:
#         print(dd,dd.puid)
    my_friend1.send(u'大家好，我是本群的提醒打卡小助手，希望看到消息的人和我一起打一次卡。三小时后我继续提醒大家打卡。和我一起成为一天打八次卡的人吧！')
    t = Timer(10800, send_notify) #360是秒数
    t.start()


if __name__ == '__main__':
    send_notify()