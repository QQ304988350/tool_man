import httpx
import asyncio
# 异步获取

async def get_async_paper_byapi():
    try:
        async with httpx.AsyncClient() as client:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
                # "Accept": "image/png,*/*;q=0.8"
            }
            res = await client.post(
                url="https://api.qqsuu.cn/api/dm-60s",
                headers=headers,
                follow_redirects=True
            )
            
            # file_path = pathlib.Path("resource/paper/paper.png")
            # async with aiofiles.open("./test.png","wb") as f:
            #     await f.write(res.content)
            
            # async with aiofiles.open("./test.png","rb") as fr:
            #     frb = await fr.read()
            #     base64_data = "base64://" + base64.b64encode(frb).decode()
            return res.content

    except Exception as e:
        return e
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_async_paper_byapi())
