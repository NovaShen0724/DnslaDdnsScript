# DnslaDdnsScript
---
### 1.简介
	自动解析ipv6地址到dnsla的python脚本 A repository of the python script to use the dns,la api
---
### 2.用法
1.在dnsla后台-我的账户-API中开启api，并记录你的appiid和api密钥(apipass)<br>
2.使用Get_recordid脚本，填入appiid和apipass以及domain_name后获取你所需ddns的记录id<br>
3.将信息填入ddns.conf中，切记休眠时间不得少于60s<br>
4.请确保脚本所在设备具有公网ipv6地址并且路由器防火墙放行(ipv6spl)<br>
### 3.依赖
1.requests(需要安装)<br>
2.json<br>
3.socket<br>
4.time<br>

# DnslaDdnsScript
---
### 1.Explanation
	It's a script for people who use dns.la to be their domain's nameservers to post thier ipv6 address currently by this automatic python project.
---
### 2.Usage
1. Open the api in the dnsla background My Account API, and record your appiid and api key (apipass)<br>
2. Use Get_ Recordid script, fill in appiid, apipass and domain_ After name, get the record ID of the ddns you need<br>
3. Fill the information into ddns.conf, and remember that the sleep time shall not be less than 60s<br>
4. Please ensure that the device where the script is located has a public network ipv6 address and the router firewall passes (ipv6 spl)<br>
### 3. Dependence
1. Requests (to be human installed)<br>
2.json<br>
3.socket<br>
4.time
