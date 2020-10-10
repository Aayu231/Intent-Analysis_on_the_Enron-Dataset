import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("enter url")
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('User count:', len(info))
c=0
s=0
for item in info:

    x = item["count"]
    c+=1
    s+=x
print("count is ", c)
print("sum is ", s)
