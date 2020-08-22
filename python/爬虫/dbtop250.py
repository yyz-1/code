from bs4 import BeautifulSoup  #网页解析
import re   #正则表达式，进行文字匹配
import urllib.request,urllib.error     #定制url，获取网页数据
import xlwt #进行excel操作
#import pymysql  #使用 mysql 数据库 ,python 自带的是sqlite3


def main():
    baseurl = "https://movie.douban.com/top250?start="
    #askURL("https://movie.douban.com/top250?start=")
    datalist = getdata(baseurl)
    savedata(datalist)


findlink = re.compile(r'<a class="" href="(.*?)">') #主页链接  #会出现四个列表的错误
#findlink = re.compile(r'<a href="(.*?)">')
findimgstr = re.compile(r'src="(.*?)"')  #图片
findtitle = re.compile(r'<span class="title">(.*)</span>')  #电影名
finddb = re.compile(r'<p class="">(.*?)</p>',re.S)   #导演主演等数据
findpf = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')      #movie 评分  (\d*)无效，数字带小数点 string类型，不是float
findpfrs = re.compile(r'<span>(\d*)人评价</span>')      #movie 评分人数
findinq = re.compile(r'<span class="inq">(.*)</span>')     #短评


def getdata(baseurl):
    datalist = []
    for i in range(0,10):    #左闭右开区间，访问十次
        url = baseurl + str(i*25)
        html = askURL(url)

        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"):
            data = []
            item = str(item)
            #print(item)

            link = re.findall(findlink,item)[0]
            #print(link)
            data.append(link)
            #print(len(data))

            imgstr = re.findall(findimgstr,item)[0] #不加一个[0] 是二层套嵌列表
            data.append(imgstr)
            #print(data)
            '''
            title_name = re.findall(findtitle,item)[0]
            data.append(title_name)
            #只写入一个中文名字
            '''
            title_name = re.findall(findtitle,item) #写入多个名字 中文 and 外文
            #print(title_name)
            if (len(title_name) == 2):
                one_title = title_name[0]   #中国名
                data.append(one_title)
                two_title = title_name[1].lstrip("/ ")  #外国名 .replace("/","")也可以替换条无关符号
                data.append(two_title)
            else:
                data.append(title_name[0])
                data.append(" ")

            movie_db = re.findall(finddb,item)[0]   # /...<br/> #...在网页中是省略号 / & <br/> remove
            movie_db = movie_db.strip()
            movie_db = re.sub("<br/>(\s+)?",'',movie_db)    #remove <br/>& (\s+)? 去空格
            movie_db = re.sub("/",'',movie_db)
            movie_db = re.sub(r'\xa0'," ",movie_db)
            data.append(movie_db)

            movie_pf = re.findall(findpf,item)[0]      #评分
            data.append(movie_pf)

            pfrs = re.findall(findpfrs,item)[0]     #平分人数
            data.append(pfrs)

            inq = re.findall(findinq,item)     #短评 一直到 地球上的星星 报错 226 七品芝麻官 没有短评
            if len(inq) != 0:
                inq = inq[0]        #这句不写会出现 列表套嵌
                data.append(inq)
            else:
                data.append(" ")    #留空
            #print(data)
            datalist.append(data)
            #print(datalist)
    return datalist


def askURL(url):
    headers = {         #请求头的伪装，模拟成正常用户使用浏览器访问
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }       

    req = urllib.request.Request(url,headers=headers)
    html = ""
    try:
        fanhui = urllib.request.urlopen(req)
        html = fanhui.read().decode("utf-8")
#        print(html)
#        print(fanhui.status)
    except urllib.error.URLError as e:
        print("error",e)    
    return html


def savedata(datalist):
    workexcle = xlwt.Workbook(encoding="utf-8",style_compression=0)  #创建exle对象 style_compression:表示是否压缩
    worksheet = workexcle.add_sheet("TOP250",cell_overwrite_ok=True)   #创建工作表 cell_overwrite_ok 是否可以复写
    columns = ("电影链接","海报链接","电影名","外国名","导演主演等","评分","评分人数","短评")
    for i in range(0,8):
        worksheet.write(0,i,columns[i]) #写入要指定 位置 （0，0）类似坐标位置
    for n in range(0,250):
        data = datalist[n]  #注意：一共250行，每行8条数据
        for x in range(0,8):
            worksheet.write(n+1,x,data[x])  #一行八条数据

    workexcle.save("豆瓣top250.xls") #保存


if __name__ == "__main__":  #程序执行时
    main()  #调用函数
    print("ok")