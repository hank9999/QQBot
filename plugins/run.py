from nonebot import on_command, CommandSession
from nonebot import permission as perm


@on_command('run', permission=perm.SUPERUSER | perm.GROUP_ADMIN, only_to_me=False)
async def runCommand(session: CommandSession):
    chat_data = str(session.current_arg_text).strip()
    if chat_data == 'help':
        message = '#run 指令'
        await session.send(message)
    elif chat_data == '':
        message = '参数不全 获取帮助 #run help'
        await session.send(message)
    else:
        result = await rcon(chat_data)
        await session.send(result)
