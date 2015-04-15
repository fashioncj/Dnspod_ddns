# -*- coding: UTF-8 -*- 
# 
# DNSPOD 的DDNS自动更新域名记录
# 需要通过官方客户端获得你的域名id和记录id，当然也可以使用他的api
# 这个版本是for linux，在ubuntu上测试成功
# 修改变量对应的数值，使用python2运行
# by：fashioncj http://blog.chenjia.me
# 返回值解析https://www.dnspod.cn/docs/records.html#dns
import urllib
import urllib2
import socket
import fcntl
import struct
from symtable import Function
# url = 'https://dnsapi.cn/Record.Modify'
url = 'https://dnsapi.cn/Record.Ddns'
login_email= '' #email@email.com
login_password= '' #password
domain_id='' #domain id
record_id='' #record id
sub_domain='' #记录值的名称 比如@，www等等
value=''

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def getip_linux():
    global value
    value=get_ip_address('eth0')
   
if __name__ == '__main__':
    getip_linux()
    values = {'login_email':login_email,
          'login_password':login_password,
          'format':'json',
          'domain_id':domain_id,
          'record_id':record_id,
#           'record_type':'A',
          'record_line':'默认',
          'sub_domain':sub_domain,
          'value':value
           }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print the_page
    