from ncatbot.client import BotClient
from ncatbot.logger import get_log
from ncatbot.message import GroupMessage, PrivateMessage

_log = get_log()
bot = BotClient()


@bot.group_event()
def on_group_message(msg: GroupMessage):
    _log.info(msg)


@bot.private_event()
def on_private_message(msg: PrivateMessage):
    _log.info(msg)
    if msg.raw_message == "test":
        bot.api.post_private_msg(
            msg.user_id, text="你好,", face=1, reply=msg.message_id
        )
    elif msg.raw_message == "ping":
        bot.api.add_at(msg.user_id).add_face(1).add_text("你好").add_face(
            2
        ).send_private_msg(msg.user_id, reply=msg.message_id)
    elif msg.raw_message == "md":
        bot.api.post_private_file(user_id=msg.user_id, markdown="README.md")
        # await bot.api.post_private_msg(msg.user_id, markdown="## 你好")


@bot.notice_event
def on_notice(msg):
    _log.info(msg)


@bot.request_event
def on_request(msg):
    _log.info(msg)


if __name__ == "__main__":
    bot.run(reload=True)
