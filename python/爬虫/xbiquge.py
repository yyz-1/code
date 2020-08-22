'''
xbiquge_book.py 为子文件，与此文件放置统一级目录，运行此文件（半成品，没有下载功能，没有实际作用。。。
'''
import re
import urllib.parse
import urllib.request
from urllib.request import urlretrieve
import bs4
import xbiquge_book


def main():
    book_name = input(r"book name? and writer name?:")
    book_name = str(book_name)
    print("书本链接\t\t\t   书名\t作者")
    #book_name = "a"
    url = "http://www.xbiquge.la/modules/article/waps.php"
    xhcs = lenindex(url,book_name)
    datalist = geturl(url,xhcs,book_name)
    for item in datalist:
        print(item)
    bkurl = input("download url:")
    print(xbiquge_book.zdzj(bkurl))


def lenindex(url,book_name):
    html = askurl(url,book_name)
    sub = "</tr>"
    xhcs = html.count(sub,0,len(html))
    xhcs = xhcs - 1
    return xhcs


findlink = re.compile(r'<td class="even"><a href="(.*?)" target="_blank">(.*?)</a></td>')
findchapter = re.compile(r'target="_blank">(.*?)</a>')
findwriter = re.compile(r'<td class="even">(.*?)</td>')
findtime = re.compile(r'<td class="odd" align="center">.*?    </td>')


def geturl(url,xhcs,book_name):
    datalist = []
    html = askurl(url,book_name)

    bfs = bs4.BeautifulSoup(html,"html.parser")
    a = 0
 
    for i in range(0,xhcs):
        for item in bfs.find_all("table",class_="grid"): #<table class="grid"
            data = []
            item = str(item)

            link = re.findall(findlink,item)[a]
            link = str(link)
            link = link.lstrip('(')
            link = link.rstrip(')')
            link = re.sub("'","",link)
            data.append(link)
            a+=1
            '''
            chapter = re.findall(findchapter,item)
            for num in range(0, len(chapter), 2):
	            l2 = chapter[num: num + 2]
	            print(l2)
            '''
            wr = re.findall(findwriter,item)
            wr = wr[1:len(wr):2]
            wr = wr[i]
            data.append(wr)
            datalist.append(data)
    return datalist
'''
        book_time = re.findall(findtime,item)
        print(book_time)
'''

def askurl(url,book_name):
    headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'

    }
    data = bytes(urllib.parse.urlencode({"searchkey": book_name}),encoding="utf-8")
    seq = urllib.request.Request(url,headers=headers,data=data)
    html = ""
    try:
        fanh = urllib.request.urlopen(seq)
        html = fanh.read().decode("utf-8")
    except Exception as e:
        print(e)

    return html


if __name__ == "__main__":
    main()
#7.22 3
#9.31
