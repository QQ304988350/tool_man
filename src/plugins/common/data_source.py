import httpx
import asyncio
from lxml import etree


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


async def baike(key):
    res = None
    async with httpx.AsyncClient() as client:
        res = await client.get("https://baike.baidu.com/search/word?word={}".format(key), headers=headers)
        try:

            if res.status_code == 302:
                first = res.headers.get("Location")
                first_url = "https:{}".format(first)
                res = await client.get(first_url, headers=headers)
                if res.status_code == 302:
                    second = res.headers.get("Location")
                    second_url = "https://baike.baidu.com"+second
                    res = await client.get(second_url, headers=headers)
            if res.status_code == 200:
                detail_str = get_desc(res.content.decode())
                if detail_str:
                    return detail_str
            else:
                return "无记录"
        except Exception as e:
            return "无记录"


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(baike("测试"))
