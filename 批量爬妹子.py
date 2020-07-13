import  requests
import re
# url ='http://www.cntour.cn/'

url="https://image.baidu.com/search/acjson"
headers={
"Referer": "https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%D0%A1%BD%E3%BD%E3&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}
urls=[]

def img_down(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "Referer": "https://image.baidu.com/search/index?tn=ba"
                   "iduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%D0%A1%BD%E3%BD%E3&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111"
    }

    data=requests.get(url=url,headers=headers)
    print(data.status_code)
    # print(data.text)
    # print(data.content)
    filename=url.split("/")[-1]
    with open("妹子图\\"+filename,"wb")as f:
        f.write(data.content)



def ajax(n):
    global url
    for i in range(1,n+1):
        n = i
        pn = n * 30
        gsm = hex(pn)[2:]

        params={
        "tn": "resultjson_com",
        "ipn": "rj",
        "ct": "201326592",

        "fp": "result",
        "queryWord": "小姐姐",
        "cl": "2",
        "lm": "1",
        "ie": "utf-8",
        "oe": "utf-8",
        "word": "小姐姐",

        "pn":pn,
        "rn": pn,
        "gsm": gsm


        }
        res=requests.get(url=url,headers=headers,params=params)
    # print(res.status_code)
    # print(res.text)
        urls=re.findall('"thumbURL":"(.*?)"',res.text)
    # print(urls)
    # print(len(urls))


    for url in urls:
        img_down(url)
        # print(url)

# for url in urls:
#     img_down(url)
    #     img_down(url)
    # print(len(urls))

        # for url in urls:
        #     img_down(url)

    # print("答应第%s业"%n)
#
# for n in range(1,4):

if __name__ == '__main__':
    ajax(3)
    # print("调用%s"%n)
    # for url in urls:
    #     print(1)
    #     img_down(url)
    #     print("调用下载")



