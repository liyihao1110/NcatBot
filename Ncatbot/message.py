from .api import BotAPI
from .settings import settings


class BaseMessage(BotAPI):
    def __init__(self, message):
        super().__init__(port_or_http=settings.port_or_http, max_ids=settings.max_ids)
        self.self_id = message.get("self_id", None)
        self.user_id = message.get("user_id", None)
        self.time = message.get("time", None)
        self.post_type = message.get("post_type", None)

class GroupMessage(BaseMessage):
    def __init__(self, message):
        super().__init__(message)
        self.group_id = message.get("group_id", None)
        self.message_type = message.get("message_type", None)
        self.sub_type = message.get("sub_type", None)
        self.raw_message = message.get("raw_message", None)
        self.font = message.get("font", None)
        self.sender = self._Sender(message.get("sender", {}))
        self.message_id = message.get("message_id", None)
        self.message_seq = message.get("message_seq", None)
        self.real_id = message.get("real_id", None)
        self.message = message.get("message", [])
        self.message_format = message.get("message_format", None)

    # __repr__用来输出对象的所有信息，每行只显示一个信息
    def __repr__(self):
        # 去除 _api 属性再展示
        return str({key: value for key, value in self.__dict__.items() if not key.startswith("_")})

    class _Sender:
        def __init__(self, message):
            self.user_id = message.get("user_id", None)
            self.nickname = message.get("nickname", None)
            self.card = message.get("card", None)

        def __repr__(self):
            return str(self.__dict__)

    async def reply(self, reply=False):
        if reply:
            self.add_reply(self.message_id)
        return await self.send_group_msg(self.group_id, clear_message=True)

class PrivateMessage(BaseMessage):
    def __init__(self, message):
        super().__init__(message)
        self.message_id = message.get("message_id", None)
        self.message_seq = message.get("message_seq", None)
        self.real_id = message.get("real_id", None)
        self.message_type = message.get("message_type", None)
        self.sender = self._Sender(message.get("sender", {}))
        self.raw_message = message.get("raw_message", None)
        self.font = message.get("font", None)
        self.sub_type = message.get("sub_type", None)
        self.message = message.get("message", [])
        self.message_format = message.get("message_format", None)
        self.target_id = message.get("target_id", None)

    # __repr__用来输出对象的所有信息，每行只显示一个信息
    def __repr__(self):
        return str({key: value for key, value in self.__dict__.items() if not key.startswith("_")})

    class _Sender:
        def __init__(self, message):
            self.user_id = message.get("user_id", None)
            self.nickname = message.get("nickname", None)
            self.card = message.get("card", None)

        def __repr__(self):
            return str(self.__dict__)

    async def reply(self, reply=False):
        if reply:
            self.add_reply(self.message_id)
        return await self.send_private_msg(self.user_id, clear_message=True)

class AllMessage(BaseMessage):
    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.group_id = message.get("group_id", None)
        self.message_type = message.get("message_type", None)
        self.sub_type = message.get("sub_type", None)
        self.raw_message = message.get("raw_message", None)
        self.font = message.get("font", None)
        self.sender = self._Sender(message.get("sender", {}))
        self.message_id = message.get("message_id", None)
        self.message_seq = message.get("message_seq", None)
        self.real_id = message.get("real_id", None)
        self.message = message.get("message", [])
        self.message_format = message.get("message_format", None)
        self.target_id = message.get("target_id", None)

    # __repr__用来输出对象的所有信息，每行只显示一个信息
    def __repr__(self):
        return str({key: value for key, value in self.__dict__.items() if not key.startswith("_")})

    class _Sender:
        def __init__(self, message):
            self.user_id = message.get("user_id", None)
            self.nickname = message.get("nickname", None)
            self.card = message.get("card", None)

        def __repr__(self):
            return str(self.__dict__)

    # TODO: 更深一步的处理message

# TODO: 更多的之后再添加...
