# _*_ coding:utf-8 _*_
# https://github.com/gaojj2000

# 实例代码采用直观的同步方式测试，实际使用建议去除 sync=True 并使用异步编程

from Ncatbot.api import BotAPI, face

user_id = 'XXX'
group_id = 'XXX'
message_id = 'XXX'
file_id = '000000XXXXXXXXXXXXXXXXXXXXXXXXXXXX35327c.6baf1797-77XXX25f8da4'
message = BotAPI(3000, sync=True)
print(message.mark_msg_as_read(group_id=group_id))  # 设置群消息已读
print(message.mark_msg_as_read(user_id=user_id))  # 设置好友消息已读
print(message.mark_group_msg_as_read(group_id=group_id))  # 设置群聊已读
print(message.mark_private_msg_as_read(user_id=user_id))  # 设置私聊已读
print(message.mark_all_as_read())  # _设置所有消息已读
print(message.delete_msg(message_id=message_id))  # 撤回消息
print(message.get_msg(message_id=message_id))  # 获取消息详情
print(message.get_image(file_id=file_id)['data'])  # 获取图片消息详情
print(message.get_record(file_id=file_id)['data'])  # 获取语音消息详情 out_format格式（mp3/amr/wma/m4a/spx/ogg/wav/flac）
print(message.get_file(file_id=file_id)['data'])  # 获取文件信息
print(message.get_group_msg_history(group_id=group_id)['data']['messages'])  # 获取群历史消息（默认20条，如果当中有撤回，实际会小于这个值）
print(message.set_msg_emoji_like(message_id=message_id, emoji_id=face.仔细分析))  # 贴表情
print(message.get_friend_msg_history(user_id=user_id, message_seq=None, count=None, reverse_order=None))  # 获取好友历史消息（默认20条，如果当中有撤回，实际会小于这个值）
print(message.get_recent_contact(count=10)['data'])  # 最近消息列表
print(message.fetch_emoji_like(message_id=message_id, emoji_id=face.流泪))  # 获取贴表情详情
print(message.get_forward_msg(message_id=message_id))  # 获取合并转发消息

# 参数过多，懒得搞，先放一边~
# print(message.send_forward_msg(group_id=group_id, text=None, prompt=None, summary=None, source=None, user_id=None))  # 发送合并转发消息
