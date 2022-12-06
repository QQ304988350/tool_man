from typing import Any, Tuple
from nonebot import on_command, on_message,on_regex,on_startswith
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message,Bot,Event
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.typing import T_State
from nonebot.params import EventPlainText
from nonebot.params import EventToMe #@之后生效
from nonebot.params import RegexGroup
from .data_source import baike
from nonebot.adapters.onebot.v11 import MessageSegment, Bot

# testMatcher = on_regex("^试试$", priority=6)


# @testMatcher.handle()
# async def onceHandle(foo: str = EventPlainText(),foo2: bool = EventToMe()):
#     await testMatcher.send("我还活着!")

# testRe = on_regex("测试(.*)", priority=6)

# @testRe.handle()
# async def onceHandle(foo: Tuple[Any, ...] = RegexGroup()):
#     print(foo,22222222222)
#     await testMatcher.send(foo[0])
# matcher = on_message()


baikeMatcher = on_startswith("百科", priority=6)
@baikeMatcher.handle()
async def onceHandle(event: Event):
    args = str(event.get_plaintext()).strip()[2:].strip()
    data = await baike(args)
    await baikeMatcher.send("百度百科: \n{}".format(data), at_sender=True)

