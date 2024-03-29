from nonebot_plugin_apscheduler import scheduler
from .data_source import get_async_paper_byapi
from typing import Any, Tuple
from nonebot import on_command, on_message, on_regex
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message, Bot, Event
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.typing import T_State
from nonebot.params import EventPlainText
from nonebot.params import EventToMe  # @之后生效
from nonebot.params import RegexGroup
from nonebot.adapters.onebot.v11 import MessageSegment, Bot
import nonebot
from nonebot import require
require("nonebot_plugin_apscheduler")

news_60s = on_regex(r"^早报$|^新闻$")


@news_60s.handle()
async def _(foo: Tuple[Any, ...] = RegexGroup()):
    content = await get_async_paper_byapi()
    await news_60s.send(MessageSegment.image(content))


@scheduler.scheduled_job("cron", day_of_week='mon-fri', hour=9, minute=30, id="news_60s")
async def _():
    schedBot = list(nonebot.get_bots().values())[0]
    content = await get_async_paper_byapi()
    group_list = ["314329481", "260726956",
                  "835093566", "1067030489", "859136792"]
    for group_id in group_list:
        try:
            await schedBot.call_api("send_msg", **{"message": MessageSegment.image(content), "group_id": group_id})
        except Exception as e:
            print(e)
            pass
