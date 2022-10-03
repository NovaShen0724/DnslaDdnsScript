import configparser
import json
import socket
import time

from requests import post


def getipv6():
    host_ipv6 = []
    ips = socket.getaddrinfo(socket.gethostname(), 80)
    for ip in ips:
        if ip[4][0].startswith('24'):
            host_ipv6.append(ip[4][0])
    return host_ipv6


cf = configparser.ConfigParser()
path = "ddns.conf"
cf.read(path, encoding='UTF-8')
dnsinfo = dict(cf.items("dnsla"))
sleeptime = int(dict(cf.items("setting"))["times"])
url = "https://api.dns.la/api/record.ashx"

while 1:
    if getipv6()[1] != '':
        ipaddress = getipv6()[1]
    else:
        ipaddress = getipv6()[0]
    print("Now ipv6 address: [" + ipaddress + "]")
    dnsinfo["recorddata"] = ipaddress
    r = post(url, params=dnsinfo)
    tt = json.loads(r.text)
    code = tt["status"]["code"]
    title = tt["status"]["name"]
    massage = tt["status"]["message"]
    print("Code " + str(code) + " " + title + " " + massage)
    if code != 300:
        break
    print("Exit successful!Now sleep " + str(sleeptime) + " sec.")
    time.sleep(sleeptime)
