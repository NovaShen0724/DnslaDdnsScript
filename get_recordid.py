from requests import post

ask = dict()
ask["cmd"] = "list"
ask["rtype"] = "json"
ask["apiid"] = input("Please enter apiid:")
ask["apipass"] = input("Please enter apipass:")
ask["domain"] = input("Please enter domain name:")
url = "https://www.dns.la/api/record.ashx"

print(post(url, params=ask).text)
kk=input("Press any key to exit.")