import urllib.request
from urllib.request import urlretrieve
import re
from bs4 import BeautifulSoup
import os
import random


def main():
    baseurl = input("url链接(访问堆糖，找到分类，随便点击，会进入新的页面，复制新的页面的网址。例:'https://www.duitang.com/category/?cat=avatar')：")
    pages = eval(input("要爬取几页图片？（一页内容为24张图片）："))
    temppath = input("要保存文件的目录：(请输入绝对路径，或要在用户目录下创建一新目录！)：")
    #if isinstance(pages,int):
    print("正在为您爬取图片ing。。。") 

    #baseurl = "https://www.duitang.com/category/?cat=avatar"
    #askurl(baseurl)
    #getdata(baseurl)
    datalist = getdata(baseurl,pages)
    getimg(datalist,temppath)


#<img data-rootid="1172802765" alt="头像" data-iid="" src="https://c-ssl.duitang.com/uploads/item/202001/10/20200110074145_uVZFy.thumb.400_0.jpeg" height="263"/>
#<img width="24" height="24" src="https://c-ssl.duitang.com/uploads/people/202008/03/20200803115334_8dNaZ.thumb.100_100_c.jpeg" />

#findurl = re.compile(r'<img data-rootid="\d*?" alt="头像" data-iid="" src=".*?" height="\d*?"/>')
#findsrc = re.compile(r'<img(.*?)src="(.*?)"(.*?)')
findsrc = re.compile(r'<img(.*?)src="(.*?)"')


def getdata(baseurl,pages):
    datalist = []
    html = askurl(baseurl)

    for i in range(0,pages):    #这里的下表表示爬取的页数

        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="woo"): #div class="woo-pcont stpics clr "
            data = []
            item = str(item)

            imgurl = re.findall(findsrc,item)[0]
            #del imgurl[0][0]   #这里的 imgurl 是元组，无法修改
            data.append(imgurl)     #列表里嵌套着元组，元组里又有两种元素
            #print(data[0][1])
            data = data[0][1]
            #print(data)

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
    except urllib.error.URLError as e:
        print("error",e)    
    return html


def getimg(datalist,temppath):
    #if os.path.isdir(temppath):
    if os.path.isfile(temppath):
        pass
    else:
        os.system('mkdir %s' % temppath)

    c = random.uniform(0,100000000)     #生成随机数文件名
    for item in datalist:
        #print(item,c)  #测试有多少链接
        urlretrieve(item,"%s/%d.jpg"%(temppath,c))
        c+=1      
    print("本次共爬取头像：%d 张"%len(datalist))

if __name__ == "__main__":
    main()
    print("ok")