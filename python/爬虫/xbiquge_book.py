import re
import urllib.parse
import urllib.request
from urllib.request import urlretrieve
import bs4
import gzip
import io
import xlwt


bkurl = "http://www.xbiquge.la/61/61960/"

def zdzj(bkurl):
    #url = "http://www.xbiquge.la/61/61960/"
    #askurl(url)
    mun = lenindex(bkurl)
    #geturl(url,mun)
    datalist = geturl(bkurl,mun)
    #savelist(datalist,mun)
    print(datalist)
    return datalist

findan = re.compile(r'<dd><a href="(.*?)">(.*?)</a></dd>') #这里链接要加上http://http://www.xbiquge.la/


def geturl(bkurl,mun):
    datalist = []
    html = askurl(bkurl)

    suop = bs4.BeautifulSoup(html,"html.parser")
    headlink = 'http://www.xbiquge.la'
    for x in range(0,mun):
        for item in suop.find_all("div",id="list"):     # <div id="list">
            data = []
            item = str(item)

            book_an = re.findall(findan,item)[x]
            book_an_url = headlink + book_an[0]
            data.append(book_an_url)
            data.append(book_an[1])
            datalist.append(data)
            
    return datalist


def askurl(bkurl):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }       

    req = urllib.request.Request(bkurl,headers=headers)
    html = ""
    try:
        fanhui = urllib.request.urlopen(req)
        '''
        html = fanhui.read()
        print(html)     #b'\x1f\x8b\x08\x00\x00  gzip
        '''
        html = fanhui.read()
        buff = io.BytesIO(html)
        f = gzip.GzipFile(fileobj=buff)
        html = f.read().decode("utf-8")
    except urllib.error.URLError as e:
        print("error",e)
    return html    


def lenindex(bkurl):
    html = askurl(bkurl)
    sub = "<dd>"
    xhcs = html.count(sub,0,len(html))
    return xhcs

'''
def savelist(datalist,mun):
    select_list = ["link","list"]
    cclist = []
    workexecl = xlwt.Workbook(encoding="utf-8")
    worksheet = workexecl.add_sheet("sheet_1",cell_overwrite_ok=True)
    for i in range(0,2):
        worksheet.write(0,i,select_list[i])

    for n in range(0,mun):       
        for a in range(0,2):
            lista = datalist[n][a]
            lista = lista.split(" ")
            cclist.append(lista)
    print(cclist)
    for i in range(0,mun):
        for x in range(0,2):
            worksheet.write(i+1,x,lista[x])
    
    #workexecl.save("bqg.xls")
'''

if __name__ == "__main__":
    zdzj(bkurl)
