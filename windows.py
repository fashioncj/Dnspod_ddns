# -*- coding: UTF-8 -*-
# 
# DNSPOD 的DDNS自动更新域名记录
# 需要通过官方客户端获得你的域名id和记录id，当然也可以使用他的api
# 这个版本是for windows，如果有多个网卡需要手动选择，输入数字即可
# 修改变量对应的数值，使用python2运行
# by：fashioncj http://blog.chenjia.me
# 返回值解析https://www.dnspod.cn/docs/records.html#dns 
import urllib
import urllib2
import socket

# url = 'https://dnsapi.cn/Record.Modify'
url = 'https://dnsapi.cn/Record.Ddns'
login_email= '' #email@email.com
login_password= '' #password
domain_id='' #domain id
record_id='' #record id
sub_domain='' #记录值的名称 比如@，www等等
value=''

def getipwindows():
    ipList = socket.gethostbyname_ex(socket.gethostname())
    ipList =ipList[2]
    i=1
    for ip in ipList:
        print "%d : %s" % (i,ip)
        i=i+1
    index=input("Please input the index of your ddns ip:\n")
    print(ipList[index-1])
    global value
    value=ipList[index-1]
   
if __name__ == '__main__':
    getipwindows()
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
    