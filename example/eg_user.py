# _*_ coding:utf-8 _*_
# https://github.com/gaojj2000

# 实例代码采用直观的同步方式测试，实际使用建议去除 sync=True 并使用异步编程

from Ncatbot.api import BotAPI, status

user_id = 'XXX'
group_id = 'XXX'
user = BotAPI(3000, sync=True)
print(user.set_qq_profile(nickname='a', personal_note='abc', sex='1'))  # 设置账号信息（nickname必须，sex 1为男，2为女）
print(user.ark_share_peer(group_id=group_id)['data']['arkJson'])  # 获取推荐好友卡片
print(user.ark_share_peer(user_id=user_id)['data']['arkMsg'])  # 获取推荐群聊卡片
print(user.ark_share_group(group_id=group_id)['data'])  # 获取推荐群聊卡片
print(user.set_online_status(**status.timi中))  # 设置在线状态（可能会有一点延迟生效）
print(user.get_friends_with_category()['data'])  # 获取好友分组列表
print(user.set_qq_avatar(file='https://apifox.com/api/v1/projects/5348325/resources/475696/image-preview'))  # 设置头像
print(user.send_like(user_id=user_id, times=20))  # 点赞（最大点赞数可设置为20，SVIP当日最高点赞20次，普通用户当日最大点赞10次，不能给自己点赞！）
print(user.create_collection(raw_data='测试内容', brief='测试标题'))  # 创建收藏
print(user.set_friend_add_request(flag='u_wyxm16XXXXuR5Cu3Q|173XXXX425', approve=True, remark='神！！！'))  # 处理好友请求
print(user.set_self_longnick(long_nick='cba'))  # 设置个性签名
print(user.get_stranger_info(user_id=user_id))  # 获取账号信息（可以获取任何QQ的，不限于自己的好友）
print(user.get_friend_list(no_cache=False))  # 获取好友列表
print(user.get_profile_like())  # 获取点赞列表
print(user.fetch_custom_face(count=10)['data'])  # 获取收藏表情
print(user.upload_private_file(user_id=user_id, file='../README.md', name='readme'))  # 上传私聊文件
print(user.delete_friend(friend_id=user_id))  # 删除好友

# 需要packetServer服务，等待开发~
# print(user.nc_get_user_status(user_id=user_id))  # 获取用户状态
# print(user.get_mini_app_ark(type_=None, title=None, desc=None, pic_url=None, jump_url=None))  # 获取小程序卡片
