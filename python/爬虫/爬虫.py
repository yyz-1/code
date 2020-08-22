import urllib.request
from urllib.request import urlretrieve
import re
from bs4 import BeautifulSoup


def main():
    baseurl = "http://www.win4000.com/zt/erciyuan_1.html"
    getdata(baseurl)
    datalist = getdata(baseurl)
    getimg(datalist)


findurl = re.compile(r'<img src=".*?"')


def getdata(baseurl):
    datalist = []
    html = askurl(baseurl)

    for i in range(0,25):

        soup = BeautifulSoup(html,"html.parser")#class_="clearfix"  <div class="w1180 clearfix">
        for item in soup.find_all("div",class_="w1180 clearfix"):  #div class="recommend_bz"div class="tab_tj"
            data = []
            item = str(item)

            imgurl = re.findall(findurl,item)[i]
            imgurl = imgurl.lstrip('<img src="')
            imgurl = imgurl.rstrip('"')
            #print(imgurl)
            data.append(imgurl)

            datalist.append(data)
    return datalist


def askurl(url):
    headers = {         #请求头的伪装，模拟成正常用户使用浏览器访问
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }       

    req = urllib.request.Request(url,headers=headers)
    html = ""
    try:
        fanhui = urllib.request.urlopen(req)
        html = fanhui.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        print("error",e)    
    return html


def getimg(datalist):
    c=0
    for item in datalist:
        i = 0   
        link = item[0]
        #path = "C:/Users/Administrator/Desktop/ppp/%d.jpg"%c
        urlretrieve(link,"C:/Users/Administrator/Desktop/ppp/%d.jpg"%c) #在桌面加一个ppp的文件夹
        #print(i)
        c+=1
        i += 1


if __name__ == "__main__":
    main()
    print("ok") 