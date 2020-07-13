url="https://movie.douban.com/top250"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
import requests
res=requests.get(url=url,headers=headers)

from lxml import etree
from lxml import html




html_data =etree.HTML(res.text)
name=html_data.xpath('//div/div/a/span[1]/text()')
print(name)



"""              <div class="pic">
                    <em class="">9</em>
                    <a href="https://movie.douban.com/subject/3541415/">
                        <img width="100" alt="盗梦空间" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p513344864.jpg" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/3541415/" class="">
                            <span class="title">盗梦空间</span>
                                    <span class="title">&nbsp;/&nbsp;Inception</span>
                                <span class="other">&nbsp;/&nbsp;潜行凶间(港)  /  全面启动(台)</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 克里斯托弗·诺兰 Christopher Nolan&nbsp;&nbsp;&nbsp;主演: 莱昂纳多·迪卡普里奥 Le...<br>
                            2010&nbsp;/&nbsp;美国 英国&nbsp;/&nbsp;剧情 科幻 悬疑 冒险
                        </p>


                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.3</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1478436人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">诺兰给了我们一场无法盗取的梦。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>

# """
# response.xpath('//div[@class="star"]/span[2]/text()')
# response.xpath('//div[@class="bd"]/p/text()')
# response.xpath('//div[@class="bd"]/p/text()').extract()[0].strip()



('./div/em/a/@href')

#  <span property="v:summary" class=""
"""<div class="item">
                <div class="pic">
                    <em class="">25</em>
                    <a href="https://movie.douban.com/subject/6786002/">
                        <img width="100" alt="触不可及" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p1454261925.jpg" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/6786002/" class="">
                            <span class="title">触不可及</span>
                                    <span class="title"> / Intouchables</span>
                                <span class="other"> / 闪亮人生(港)  /  逆转人生(台)</span>
                        </a>


                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 奥利维·那卡什 Olivier Nakache / 艾力克·托兰达 Eric Toledano   主...<br>
                            2011 / 法国 / 剧情 喜剧
                        </p>


                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.2</span>
                                <span property="v:best" content="10.0"></span>
                                <span>716512人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">满满温情的高雅喜剧。</span>
                            </p>
                    </div>
                </div>
            </div>

"""