# Dnspod_ddns
Dnspod自动更新域名记录，实现DDNS的功能。使用官方接口，支持windows和linux。官方api网站：https://www.dnspod.cn/docs/records.html#dns

#请阅读对应py文件中的注释
+ windows 支持多网卡选择
+ linux 默认选择“eth0”网卡ip
+ 如果更新的ip和外网请求的ip一致，注释掉这一行：
	+ `          'value':value`
	
	

---
[http://blog.chenjia.me](http://blog.chenjia.me)