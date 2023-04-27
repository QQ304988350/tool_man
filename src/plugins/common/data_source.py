import httpx
import asyncio
from lxml import etree
from nonebot.adapters.onebot.v11 import MessageSegment, Bot,Message


headers = {
    "Content-Type": "text/html; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43"

}


def get_desc(html_str):
    html = etree.HTML(html_str)
    detail: str = html.xpath(
        '//div[@class="lemma-summary"]/div[@class="para"]//text()')
    detail_str = " ".join(detail)
    print(detail_str)
    return detail_str


async def get_baike(key_name):
    async with httpx.AsyncClient() as client:
        try:
            res = await client.get(f"http://baike.baidu.com/api/openapi/BaikeLemmaCardApi?scope=103&format=json&appid=379020&bk_key={key_name}&bk_length=1200")
            if res.status_code == 200:
                data = res.json()
                if data:
                    mixed_msg = Message()
                    mixed_msg.append(MessageSegment.image(data["image"]))
                    mixed_msg.append(data["abstract"])
                    return mixed_msg
                else:
                    return "未收录该词条"
            else:
                return "接口异常,请稍后重试"

        except Exception as e:
            print("查询失败:{}".format(e))
            return "查询失败"



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_baike("测试"))
