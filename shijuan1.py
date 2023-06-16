"""
 * @Author: Rain
 * @Date: 2023-06-13 13:44:21
 * @Last Modified by:   Rain 
 * @Last Modified time: 2023-06-13 13:44:21  
"""

import requests
from bs4 import BeautifulSoup
import urllib3
import os
import rarfile
import filetype
import random
# import zipfile
from urllib.request import urlretrieve
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# 爬取网页
# https://www.shijuan1.com/a/sjyw1/
# https://www.shijuan1.com/a/sjsx1/
# https://www.shijuan1.com/a/sjyy1/
# https://www.shijuan1.com/a/sjwl8/
# https://www.shijuan1.com/a/sjhx9/
# https://www.shijuan1.com/a/sjzz7/
# https://www.shijuan1.com/a/sjls7/
# https://www.shijuan1.com/a/sjdl7/
# https://www.shijuan1.com/a/sjsw7/
headers_list = [
    {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666'
    }, {
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320'
    }, {
        'user-agent': 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+'
    }, {
        'user-agent': 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)'
    }, {
        'user-agent': 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    }, {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    }
]

headers = random.choice(headers_list)

subject_list=["https://www.shijuan1.com/a/sjyw",
            "https://www.shijuan1.com/a/sjsx",
            "https://www.shijuan1.com/a/sjyy",
            "https://www.shijuan1.com/a/sjwl",
            "https://www.shijuan1.com/a/sjhx",
            "https://www.shijuan1.com/a/sjzz",
            "https://www.shijuan1.com/a/sjls",
            "https://www.shijuan1.com/a/sjdl",
            "https://www.shijuan1.com/a/sjsw"]
number_list=["1","2","3","4","5","6","7","8","9","zk","gk","g1","g2","g3"]

# 发起请求，获取所有网页信息，get方法会返回一个响应对象。获取响应数据
def get_page_content(url):
    proxies = { "http": None, "https": None}
    try:
        response = requests.get(url=url,stream=True, headers=headers,proxies=proxies, verify=False,timeout=10) 
        # response.close()
    except:
        for i in range(4):  # 循环去请求网站
            response = requests.get(url=url,stream=True, proxies=proxies, headers=headers,verify=False,timeout=20) 
            if response.status_code == 200:
                break
    if response.status_code == 200:
        try:
            return response.text.encode('iso-8859-1').decode('gbk')
        except:
             print('打开文件失败:%s'%(url))
             return
    else:
        print("Error accessing page:", response.status_code)
        return None
# 获取所有的链接
def extract_links(content):
    soup = BeautifulSoup(content, "html.parser")
    links=[]
    # 您可能需要根据实际网站结构调整这里的选择器
    # tr里面的第一个a
    table_elements = soup.find_all('table')
    for tr_item in table_elements:
        tr_elements = tr_item.find_all('tr')
        for a_item in tr_elements:
            # <class 'bs4.element.Tag'>
            a_elements = a_item.find('a')
            if a_elements is None:
                pass
            else:
                links.append("https://www.shijuan1.com/"+a_elements['href'])
    return links

# 点击链接进入子页面抓取内容
# content为子页面的链接
def extract_data(nextUrl):
    detail_html = get_page_content(nextUrl)
    if detail_html != None:
        soup = BeautifulSoup(detail_html, "html.parser")
        # <ul class="downurllist"><li><a href="/uploads/soft/sj2022/yuwen/1/1-221014001I1.rar" target="_blank">本地下载</a></li></ul>
        ul_list = soup.find(class_ = "downurllist")
        down_url = "https://www.shijuan1.com" + ul_list.find('a')['href']
        return down_url

# 下载资源, 并保存到本地
def downloadRar(downUrl, subject, number):
    # 指定下载路径
    # "https://www.shijuan1.com/uploads/soft/sj2022/yuwen/1/1-221014002338.rar" 
    rar_path = downUrl
    # 解压文件路径
    extract_path = "E:/ShiJuan1/" + subject[-4:] + "/" + str(number)
    # 创建解压文件夹
    # 如果exist_ok为True，则在目标目录已存在的情况下不会触发FileExistsError异常。
    os.makedirs(extract_path, exist_ok=True)
    proxies = { "http": None, "https": None}
    # 解压RAR文件
    # urlretrieve(rar_path,extract_path )
    # open的第一个参数应该是文件名
    proxies = { "http": None, "https": None}
    try:
        r = requests.get(url=rar_path,stream=True, headers=headers,proxies=proxies, verify=False, timeout=(3,7)).content
        # r.close()
    except:
        print("错了")
        return 
    rarfile_path = extract_path + '/downfile.rar'
    with open(rarfile_path,'wb') as fp:
        fp.write(r)
        # 解压
        kind = filetype.guess(rarfile_path)
        if kind is None:
            print('Cannot guess file type!')
            return
        if kind.extension != 'rar':
            print('--Not a RAR file--')
            return
        with rarfile.RarFile(rarfile_path) as rf:
            for name in rf.namelist():
                if name.endswith('.doc'):
                    extract_file = os.path.join(extract_path, name)
                    os.makedirs(os.path.dirname(extract_file), exist_ok=True)   
                    # print(name)
                    with open(extract_file, 'wb') as f:
                        f.write(rf.read(name))  

# 从首页获取其他页的url，每个年级的每个科目的试卷不只一页卷子。
# 根据url的格式，只需要获取末页的url。
# 返回一个列表
def getUrllist(baseUrl):
    html = get_page_content(baseUrl)
    if html != None:
        soup = BeautifulSoup(html, "html.parser")
        ul_list = soup.find(class_ = "pagelist")
        # ul > li > a href
        a_last = ul_list.find_all('a')[-1]['href']
        # print(a_last)
        # list_106_2.html
        for i in range(len(a_last) - 6 - 1, -1, -1): 
            if(a_last[i] >= '0' and a_last[i] <= '9'):
                continue
            else:
                break
        last_number = int(a_last[i + 1 : len(a_last) - 5])
        page_list = []
        for page in range(last_number):
            page_list.append(baseUrl + a_last[0 : i + 1]+str(page + 1) + a_last[-5 : ])
        return page_list
    # 所有页的列表


def main():
    for subject in subject_list:
        for number in number_list:
            baseUrl = subject + number + "/"
            #print(baseUrl)
            print("---")
            page_list = getUrllist(baseUrl)
            for page_url in page_list:
                origin_html = get_page_content(page_url)
                if origin_html != None:
                    link_list = extract_links(origin_html)
                for link in link_list:
                    downloadRar(extract_data(link), subject ,number)

if __name__ == "__main__":
    main()
