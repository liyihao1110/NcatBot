# _*_ coding:utf-8 _*_
# https://github.com/gaojj2000

# 实例代码采用直观的同步方式测试，实际使用建议去除 sync=True 并使用异步编程

from Ncatbot.api import BotAPI

user_id = 'XXX'
group_id = 'XXX'
system = BotAPI(4000, sync=True)
print(system.get_robot_uin_range())  # 获取机器人账号范围
print(system.ocr_image(image='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'))  # OCR 图片识别
print(system.translate_en2zh())  # 英译中
print(system.get_login_info())  # 获取登录号信息
print(system.set_input_status(event_type=0, user_id=user_id))  # 设置输入状态
print(system.download_file(url='https://file.upfile.live/uploads/20241125/8f607e4bbaa4a6ab1f484bbbca51cc2b.7z', thread_count=8, name='v2rayN-windows-64-SelfContained-With-Core.7z'))  # 下载文件到缓存目录（Tencent Files/NapCat/temp）
print(system.get_cookies(domain='user.qzone.qq.com'))  # 获取 QQ空间 cookies
print(system.get_csrf_token())  # 获取 CSRF Token
print(system.del_group_notice(group_id=group_id, notice_id='047d172dXXXXXXXXd19e0000'))  # _删除群公告
print(system.get_credentials(domain='user.qzone.qq.com'))  # 获取 QQ空间 相关接口凭证
print(system.get_model_show(model=''))  # _获取在线机型
print(system.can_send_image())  # 检查是否可以发送图片
print(system.nc_get_packet_status())  # 获取packet状态（太菜了，没看懂 https://napneko.github.io/config/advanced#%E9%85%8D%E7%BD%AE-packetbackend ）X
print(system.can_send_record())  # 检查是否可以发送语音
print(system.get_status())  # 获取状态
print(system.nc_get_rkey())  # 获取rkey（太菜了，没看懂 https://napneko.github.io/config/advanced#%E9%85%8D%E7%BD%AE-packetbackend ）X
print(system.get_version_info())  # 获取版本信息

# 不知道为啥返回老报错,先丢一边~
# print(system.get_group_shut_list(group_id=group_id))  # 获取群禁言列表 X
