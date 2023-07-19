#Version:a, by Gimi Huang

#Before use it, you should replace _IP_ / _PORT_ / user-agent / _FOLDER_

#load
from time import time
import requests
import re

#proxy setting
#socks.set_default_proxy(socks.SOCKS5,"_IP_",_PORT_)
#socket.socket = socks.socksocket

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

#only for 7 days
for image_num in range(0,7):
    timestamp = time()
    image_url='https://www.bing.com/HPImageArchive.aspx?format=js&idx=' + str(image_num) + '&n=1&nc=' + str(int(timestamp*1000)) + '&pid=hp&mkt=en-US'
    r = requests.get(url=image_url,headers=headers)
    result = r.json()
    image_url = result['images'][0]['url']
    image_date = result['images'][0]['startdate']
    image_title = result['images'][0]['title']
    image_title = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）]+".encode('utf-8').decode('utf-8'), " ", image_title)
    image_title = image_date + '-' + image_title + '.jpg'
    image_url = 'https://www.bing.com' + image_url.replace('1920x1080', 'UHD')
    #image_url = 'https://cn.bing.com' + image_url.replace('1920x1080', 'UHD')
    save_image_file = '_FOLDER_(like Z:\\bing\\)' + image_title
    r = requests.get(url=image_url, headers=headers)
    with open(save_image_file, 'wb') as f:
        f.write(r.content)