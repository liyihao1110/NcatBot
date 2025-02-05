import json
from enum import Enum
from typing import Union


class MessageChain:
    def __init__(self, chain=None):
        self.chain = []
        if chain is None:
            return

        if isinstance(chain, str):
            try:
                # 尝试解析JSON字符串，保持列表顺序
                parsed_chain = json.loads(chain)
                if isinstance(parsed_chain, list):
                    self.chain = parsed_chain
                else:
                    self.chain = [Text(chain)]
            except json.JSONDecodeError:
                self.chain = [Text(chain)]
        elif isinstance(chain, list):
            # 直接使用传入的列表，保持原有顺序
            self.chain = list(chain)  # 创建新列表以避免引用问题

    def __str__(self):
        """确保字符串表示时保持顺序"""
        return json.dumps(self.chain, ensure_ascii=False)

    @property
    def elements(self) -> list:
        """将消息链转换为可序列化的字典列表"""
        return self.chain

    def __add__(self, other):
        """支持使用 + 连接两个消息链"""
        if isinstance(other, MessageChain):
            return MessageChain(self.chain + other.chain)
        return MessageChain(self.chain + [other])

    def display(self) -> str:
        """获取消息链的字符串表示"""
        result = []
        for elem in self.chain:
            if elem["type"] == "text":
                result.append(elem["data"]["text"])
            elif elem["type"] == "image":
                result.append("[图片]")
            elif elem["type"] == "at":
                result.append(f"@{elem['data']['qq']}")
            elif elem["type"] == "face":
                result.append("[表情]")
            elif elem["type"] == "music":
                result.append("[音乐]")
            elif elem["type"] == "video":
                result.append("[视频]")
            elif elem["type"] == "dice":
                result.append("[骰子]")
            elif elem["type"] == "rps":
                result.append("[猜拳]")
            elif elem["type"] == "json":
                result.append("[JSON]")
        return "".join(result)


class Element:
    """消息元素基类"""

    type: str = "element"

    def __new__(cls, *args, **kwargs):
        """直接返回字典而不是类实例"""
        instance = super().__new__(cls)
        instance.__init__(*args, **kwargs)
        return instance.to_dict()


class Text(Element):
    type = "text"

    def __init__(self, text: str):
        self.text = text

    def to_dict(self) -> dict:
        return {"type": "text", "data": {"text": self.text}}


class At(Element):
    type = "at"

    def __init__(self, qq: Union[int, str]):
        self.qq = qq

    def to_dict(self) -> dict:
        return {"type": "at", "data": {"qq": self.qq}}


class AtAll(Element):
    type = "at"

    def as_dict(self):
        return {"type": "at", "data": {"qq": "all"}}


class Image(Element):
    type = "image"

    def __init__(self, path: str):
        self.path = path

    def to_dict(self) -> dict:
        return {"type": "image", "data": {"file": self.path}}


class Face(Element):
    type = "face"

    def __init__(self, face_id: int):
        self.id = face_id

    def to_dict(self) -> dict:
        return {"type": "face", "data": {"id": self.id}}


class PokeMethods(str, Enum):
    ChuoYiChuo = "ChuoYiChuo"
    BiXin = "BiXin"
    DianDian = "DianDian"


class Poke(Element):
    type = "poke"

    def __init__(self, method: Union[PokeMethods, str]):
        self.method = method

    def to_dict(self) -> dict:
        return {"type": "poke", "data": {"type": self.method}}


class Reply(Element):
    """回复消息元素"""

    type = "reply"

    def __init__(self, message_id: Union[int, str]):
        self.message_id = str(message_id)

    def to_dict(self) -> dict:
        return {"type": "reply", "data": {"id": self.message_id}}


class Json(Element):
    """JSON消息元素"""

    type = "json"

    def __init__(self, data: str):
        self.data = data

    def to_dict(self) -> dict:
        return {"type": "json", "data": {"data": self.data}}


class Record(Element):
    """语音消息元素"""

    type = "record"

    def __init__(self, file: str):
        self.file = file

    def to_dict(self) -> dict:
        return {"type": "record", "data": {"file": self.file}}


class Video(Element):
    """视频消息元素"""

    type = "video"

    def __init__(self, file: str):
        self.file = file

    def to_dict(self) -> dict:
        return {"type": "video", "data": {"file": self.file}}


class Dice(Element):
    """骰子消息元素"""

    type = "dice"

    def to_dict(self) -> dict:
        return {"type": "dice"}


class Rps(Element):
    """猜拳消息元素"""

    type = "rps"

    def to_dict(self) -> dict:
        return {"type": "rps"}


class Music(Element):
    """音乐分享消息元素"""

    type = "music"

    def __init__(self, type: str, id: str):
        self.music_type = type
        self.music_id = id

    def to_dict(self) -> dict:
        return {"type": "music", "data": {"type": self.music_type, "id": self.music_id}}


class CustomMusic(Element):
    """自定义音乐分享消息元素"""

    type = "music"

    def __init__(
        self, url: str, audio: str, title: str, image: str = "", singer: str = ""
    ):
        self.url = url
        self.audio = audio
        self.title = title
        self.image = image
        self.singer = singer

    def to_dict(self) -> dict:
        return {
            "type": "music",
            "data": {
                "type": "custom",
                "url": self.url,
                "audio": self.audio,
                "title": self.title,
                "image": self.image,
                "singer": self.singer,
            },
        }
