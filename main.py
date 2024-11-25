# main.py
import asyncio

from Ncatbot.websockNB import core
from Ncatbot.message import GroupMessage,PrivateMessage

# 创建 WebSocket 客户端实例并传入已注册了处理函数的 BotClient 实例
bot_websocket, botapi = core(3000, 3001)
bot_client = bot_websocket.client

# 使用装饰器注册 message 事件处理函数，并监听群聊和私聊
@bot_client.message(['group'])
async def reply_group(message: GroupMessage):
    print(message)
    if message.raw_message == "你好":
        await message.add_text('hi').add_face(4).add_text('你好').reply()
    elif message.raw_message == "hello":
        await message.rps().reply(reply=True)

@bot_client.message(['private'])
async def reply_private(message: PrivateMessage):
    print(message)
    if message.raw_message == "hi":
        await message.rps().reply()

# 使用装饰器注册 message_sent 事件处理函数，并监听群聊事件
@bot_client.message_sent(['group'])
async def reply_sent(message: GroupMessage):
    print(f"Handling sent message: {message}")
    if message.raw_message == "hi":
        await message.add_text('hello').reply()

"""
不能使用暂时
"""
# 使用装饰器注册 request 事件处理函数，并监听好友申请事件
@bot_client.request(['friend'])
def reply_request(message):
    print(f"Handling request: {message}")

# 使用装饰器注册 notice 事件处理函数
@bot_client.notice
def reply_notice(message):
    print(f"Handling notice: {message}")


# 启动 WebSocket 客户端
asyncio.run(bot_websocket.ws_run())