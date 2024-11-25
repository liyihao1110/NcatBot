# _*_ coding:utf-8 _*_
# https://github.com/gaojj2000

# 实例代码采用直观的同步方式测试，实际使用建议去除 sync=True 并使用异步编程

from Ncatbot.api import BotAPI

# 随意示例，要哪个加哪个~

group_id = 'XXX'
message_chain = BotAPI(3000, sync=True)
print(message_chain.add_text('这是我要发的图片').add_image('https://apifox.com/api/v1/projects/5348325/resources/475696/image-preview').add_text('怎么样？').send_group_msg(group_id))
print(message_chain.add_record('XXX').send_group_msg(group_id))
# 如果要获取当前发送消息的id，可以这样获取
print(message_chain.add_text('测试').add_face(4).add_text('表情可爱吧~').send_group_msg(group_id).message_ids[-1])
