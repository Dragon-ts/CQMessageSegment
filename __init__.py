from CQMessageSegment.adapters.onebot.v12 import CQMessageSegment
import asyncio


async def main():
    test_message = ''
    f'''
    这里填写CQ码,例如
    test_message = '[CQ:image,file=file://1.jpg]这是图片[CQ:at,qq=1]'
    '''
    CQ = CQMessageSegment(test_message)
    print(CQ.CQtoMessageSegment())

if __name__ == '__main__':
    asyncio.run(main())