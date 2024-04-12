from nonebot.adapters.onebot.v12.message import Message, MessageSegment
import re

from CQMessageSegment.exception.exception import IllegalCQCodeError


class CQMessageSegment:
    def __init__(self, message: str | Message):
        self.message = message
    def __str__(self):
        return 0

    def CQtoMessageSegment(self):
        if type(self.message) == str:
            message = self.message
            msg = Message()
            result = re.findall(r'\[CQ:(\w+),(\w+)=([^,\]]+)]', string=self.message)
            for i in result:
                message = message.replace(f'[CQ:{i[0]},{i[1]}={i[2]}]', '\u0000\u0f0f')
            message_list = [item for item in message.split('\u0000\u0f0f') if item != '']
            print(message_list)
            for i in result:
                match i[0]:
                    case 'at':
                        msg.append(MessageSegment.mention(i[2]))
                    case 'reply':
                        msg.append(MessageSegment.reply(i[2]))
                    case 'image':
                        msg.append(MessageSegment.image(i[2]))
            return msg
        else:
            raise IllegalCQCodeError(str(self.message))
