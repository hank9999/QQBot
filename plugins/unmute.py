from nonebot import on_command, CommandSession
from nonebot import permission as perm


@on_command('unmute', aliases=('解除禁言', '解禁'), permission=perm.GROUP_MEMBER, only_to_me=False)
async def unmuteCommand(session: CommandSession):
    chat_data = str(session.current_arg_text).strip()
    if chat_data == 'help':
        message = '#unmute 用户名'
    else:
        if chat_data != '':
            await rcon('unmute ' + chat_data)
            message = '已解除禁言' + chat_data
        else:
            message = '参数不全 获取帮助 #unmute help'
    await session.send(message)
