 # coding=utf-8
import urllib
import re

def getHtml(url):
    movies= urllib.urlopen(url)
    html = movies.read()
    return html

def getcontent(html):
    pattern ='"MovieName":"(.*?)".*?"BoxOffice":"[0-9]{3,10}"'
    result = re.findall(pattern, html)
    for i in result:
        print i
    return result

def save(html):
    f = open('2017.txt', 'w')
    f.write(html)
    f.close()

str_movie = ""
try:
    for i in range(39):
        i = i +1
        print i
        html = getHtml("http://www.cbooo.cn/Mdata/getMdata_movie?area=50&type=0&year=2017&initial=%E5%85%A8%E9%83%A8&pIndex=" + str(i))
        m = getcontent(html) #这里的得到的是列表
        str_movie +='\n'.join(m)
        # print str_movie
    save(str_movie)
except:
    save(str_movie)



