from mcrcon import MCRcon
from mcrcon_setting import rcon_setting
import re
from nonebot import on_command, CommandSession
from nonebot import permission as perm

@on_command('run', permission=perm.SUPERUSER | perm.GROUP_ADMIN, only_to_me=False)
async def run(session: CommandSession):
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


async def rcon(_command: str) -> str:
    with MCRcon(rcon_setting['address'], rcon_setting['password'], rcon_setting['port']) as mcr:
        r = mcr.command(_command)
    r = re.sub('§[0-9]', '', r)
    r = re.sub('§[a-f]', '', r)
    r = re.sub('§[k-o]', '', r)
    r = r.replace('§r', '')
    return f'{r}'