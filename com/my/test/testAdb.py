# coding: GBK
# �����Ļ΢��ͼ������΢�ţ������һ����ϵ��/Ⱥ������һ����ʱ��Ϣ  
  
import sys  
import os  
import re  
import time  

sys.path.append('D:\Python2.7.17\Lib\site-packages\androidviewclient-15.8.1-py2.7.egg')

from com.dtmilano.android.viewclient import ViewClient  
  
def test():  
    # �����ֻ�  
    device, serialno = ViewClient.connectToDeviceOrExit()  
    vc = ViewClient(device, serialno)  
    # ��HOME��  
    device.press('KEYCODE_HOME')  
    time.sleep(3)  
    # �ҵ�΢��ͼ��  
    vc.dump()  
    weixin_button = vc.findViewWithTextOrRaise(u'΢��')  
    # ���΢��ͼ��  
    weixin_button.touch()  
    time.sleep(10)  
    # �ҵ���һ����ϵ��/Ⱥ  
    # ����ʹ��UI Automator Viewer�鿴����Ӧ��һ����ϵ��/Ⱥ��resource-idΪ"com.tencent.mm:id/auj"  
    vc.dump()  
    group_button = vc.findViewByIdOrRaise("com.tencent.mm:id/auj")  
    # �����Ⱥ  
    group_button.touch()  
    time.sleep(5)  
    # �ҵ���������뵱ǰʱ��  
    vc.dump()  
    vc.findViewByIdOrRaise("com.tencent.mm:id/aep").setText('Now:{}'.format(time.strftime('%Y-%m-%d %H:%M:%S')))  
    time.sleep(3)  
    # ������Ͱ�ť  
    vc.dump()  
    vc.findViewWithTextOrRaise(u'����').touch()  
        
if __name__ == '__main__':  
    test()  