
import httpx
async def get_async_paper_byapi():
    try:
        async with httpx.AsyncClient() as client:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
                # "Accept": "image/png,*/*;q=0.8"
            }
            data = {
                "format": "image",
                "token": "2qz0tOaBsCGCF0Pe"
            }
            res = await client.post(
                url="https://v2.alapi.cn/api/zaobao",
                data=data,
                headers=headers,
                follow_redirects=True
            )
            
            # file_path = pathlib.Path("resource/paper/paper.png")
            # async with aiofiles.open(file_path,"wb") as f:
            #     await f.write(res.content)
            
            # async with aiofiles.open(file_path,"rb") as fr:
            #     frb = await fr.read()
            #     base64_data = "base64://" + base64.b64encode(frb).decode()
            return res.content

    except Exception as e:
        return e
