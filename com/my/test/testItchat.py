#coding:utf-8
'''
Created on 2020年1月25日

@author: HEWEI
'''

import itchat

itchat.auto_login()
users=itchat.search_friends("张韵")
userName= users[0]['UserName']
print(userName)
itchat.send('你好',toUserName=userName)

if __name__ == '__main__':
    pass