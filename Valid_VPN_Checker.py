# # #To extract self-IP..
# #
# #
#
import requests
response=requests.get('https://ipinfo.io/json')
print(response.json())
# #
# #
# #
# # #To check valid proxies..
# #
# #
# #
import threading
import requests
import queue

q=queue.Queue()
valid_proxies=[]

with open('proxy.txt','r') as file:
    proxies=file.read().split('\n')
    for i in proxies:
        q.put(i)

def check_proxy():
    global q
    while not q.empty():
        proxy=q.get()
        try:
            response=requests.get('https://ipinfo.io/json',
                                  proxies={'http':proxy,'https':proxy})
        except:
            continue
        if response.status_code==200:
            print(proxy)
for j in range(10):
    threading.Thread(target=check_proxy).start()
    

# #
# #
# ####################################################
# #
# #
# #After rotating proxy we'll pick one of the valid proxies and put it here to check the origin..
#
#
import requests

proxies = {'http': 'http://190.104.245.86:8080'}
response = requests.get('http://httpbin.org/ip', proxies=proxies)
print(response.json())
