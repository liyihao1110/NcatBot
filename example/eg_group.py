# _*_ coding:utf-8 _*_
# https://github.com/gaojj2000

# 实例代码采用直观的同步方式测试，实际使用建议去除 sync=True 并使用异步编程

from Ncatbot.api import BotAPI

user_id = 'XXX'
group_id = 'XXX'
message_id = 'XXX'
group = BotAPI(4000, sync=True)
print(group.set_group_kick(group_id=group_id, user_id=user_id))  # 群踢人（默认不拉黑）
print(group.set_group_ban(group_id=group_id, user_id=user_id, duration=60))  # 群禁言（禁言时长单位秒）
print(group.get_group_system_msg(group_id=group_id))  # 获取群系统消息
print(group.get_essence_msg_list(group_id=group_id))  # 获取群精华消息
print(group.set_group_whole_ban(group_id=group_id, enable=False))  # 全体禁言（默认为True）
print(group.set_group_portrait(group_id=group_id, file='XXXXX'))  # 设置群头像
print(group.set_group_admin(group_id=group_id, user_id=3181596639, enable=True))  # 设置群管理（默认为False）
print(group.set_group_card(group_id=group_id, user_id=user_id, card=''))  # 设置群成员名片（为空则为取消群名片）
print(group.delete_essence_msg(message_id=message_id))  # 删除群精华消息
print(group.set_group_name(group_id=group_id, group_name='测试'))  # 设置群名
print(group.set_group_leave(group_id=group_id))  # 退群
print(group.send_group_notice(group_id=group_id, content='测试', image="本地图片路径"))  # _发送群公告（测试只能本地图片路径）
print(group.get_group_notice(group_id=group_id))  # _获取群公告
print(group.upload_group_file(group_id=group_id, file='XXX', name='XXX', folder_id='/b9d983XXXXX2294c3e'))  # 上传群文件
print(group.set_group_add_request(flag='756514052|1732552489075532|7'))  # 处理加群请求（approve默认为True，默认同意申请）
print(group.get_group_info(group_id=group_id))  # 获取群信息
print(group.get_group_info_ex(group_id=group_id))  # 获取群信息ex
print(group.create_group_file_folder(group_id=group_id, folder_name='测试'))  # 创建群文件文件夹
print(group.delete_group_file(group_id=group_id, file_id='0000010XXXXXXXXXxxxxx2346561326137'))  # 删除群文件
print(group.delete_group_folder(group_id=group_id, folder_id='/b9d983XXXXXXX294c3e'))  # 删除群文件夹
print(group.get_group_file_system_info(group_id=group_id)['data'])  # 获取群文件系统信息
print(group.get_group_root_files(group_id=group_id)['data']['files'])  # 获取群根目录文件列表
print(group.get_group_root_files(group_id=group_id)['data']['folders'])  # 获取群根目录目录列表
print(group.get_group_files_by_folder(group_id=group_id, folder_id='/b9d983XXXXX2294c3e')['data']['files'])  # 获取群子目录文件列表（数量file_count为空没数，应该能获取全部）
print(group.get_group_files_by_folder(group_id=group_id, folder_id='/b9d983XXXXX2294c3e')['data']['folders'])  # 获取群子目录目录列表（数量file_count为空没数，应该能获取全部）
print(group.get_group_list(no_cache=False)['data'])  # 获取群列表
print(group.get_group_member_info(group_id=group_id, user_id=user_id)['data'])  # 获取群成员信息
print(group.get_group_member_list(group_id=group_id)['data'])  # 获取群成员列表
print(group.get_group_honor_info(group_id=group_id)['data'])  # 获取群荣誉
print(group.get_group_at_all_remain(group_id=group_id)['data'])  # 获取群 @全体成员 剩余次数
print(group.get_group_ignored_notifies(group_id=group_id)['data'])  # 获取群过滤系统消息

# 有【BUG】【BUG】【BUG】【BUG】【BUG】【BUG】【BUG】【BUG】【BUG】【BUG】【BUG】【BUG】【BUG】【BUG】【BUG】【BUG】【BUG】【BUG】
# print(group.set_essence_msg(message_id=message_id))  # 设置群精华消息（目前自己发的消息自己能稳定添加群精华，但别人发的消息可能会无法添加精华消息）
# 需要packetServer服务，等待开发~
# print(group.set_group_special_title(group_id=group_id, user_id=user_id, special_title='测试'))  # 设置群头衔
# print(group.get_group_file_url(group_id=group_id, file_id='XXXXX'))  # 获取群文件资源链接
# print(group.get_ai_characters(group_id=group_id, chat_type=0))  # 获取AI语音人物
# print(group.send_group_ai_record(group_id=group_id, character='0', text='测试'))  # 发送群AI语音
# print(group.get_ai_record(group_id=group_id, character='0', text='测试'))  # 获取AI语音
# 报错
# print(group.set_group_sign(group_id=group_id))  # 设置群打卡
# print(group.send_group_sign(group_id=group_id))  # 发送群打卡
