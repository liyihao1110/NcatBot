from ncatbot.client import BotClient
from ncatbot.element import At, MessageChain, Text
from ncatbot.logger import get_log
from ncatbot.message import GroupMessage, PrivateMessage

_log = get_log()
bot = BotClient()


@bot.group_event()
async def on_group_message(msg: GroupMessage):
    _log.info(msg)
    if msg.raw_message == "test1":
        # 使用 MessageChain 发送复合消息
        message = MessageChain(
            [
                Text("你好！"),
                At(msg.user_id),
                Text("\n这是一个测试消息"),
            ]
        )
        await bot.api.send_group_msg(group_id=msg.group_id, message=message)


@bot.private_event()
async def on_private_message(msg: PrivateMessage):
    _log.info(msg)
    if msg.raw_message == "test":
        await bot.api.post_private_msg(
            msg.user_id, text="你好,", face=1, reply=msg.message_id
        )
    elif msg.raw_message == "ping":
        await bot.api.add_at(msg.user_id).add_face(1).add_text("你好").add_face(
            2
        ).send_private_msg(msg.user_id, reply=msg.message_id)
    elif msg.raw_message == "md":
        await bot.api.post_private_file(user_id=msg.user_id, markdown="README.md")
        # await bot.api.post_private_msg(msg.user_id, markdown="## 你好")


@bot.notice_event
async def on_notice(msg):
    _log.info(msg)


@bot.request_event
async def on_request(msg):
    _log.info(msg)


if __name__ == "__main__":
    bot.run(reload=True)
