from nonebot import on_command, CommandSession
from nonebot import permission as perm


@on_command('mute', aliases='禁言', permission=perm.GROUP_MEMBER, only_to_me=False)
async def muteCommand(session: CommandSession):
    chat_data = str(session.current_arg_text).strip()
    if chat_data == 'help':
        message = '#mute 用户名 时间 原因'
    else:
        try:
            _name, _time, _reason = map(str, chat_data.split())
            await rcon('mute ' + _name + ' ' + _time + ' ' + _reason)
            message = '已禁言: ' + str(_name) + ' 时长: ' + str(_time) + ' 原因: ' + str(_reason)
        except Exception:
            message = '参数不全 获取帮助 #mute help'
    await session.send(message)

