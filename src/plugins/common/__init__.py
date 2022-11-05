from typing import Any, Tuple
from nonebot import on_command, on_message,on_regex
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message,Bot,Event
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.typing import T_State
from nonebot.params import EventPlainText
from nonebot.params import EventToMe #@之后生效
from nonebot.params import RegexGroup

# testMatcher = on_regex("^试试$")


# @testMatcher.handle()
# async def onceHandle(foo: str = EventPlainText(),foo2: bool = EventToMe()):
#     await testMatcher.send("我还活着!")

# testRe = on_regex("测试(.*)")

# @testRe.handle()
# async def onceHandle(foo: Tuple[Any, ...] = RegexGroup()):
#     print(foo,22222222222)
#     await testMatcher.send(foo[0])
# matcher = on_message()
