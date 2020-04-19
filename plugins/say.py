from mcrcon import MCRcon
from mcrcon_setting import rcon_setting
from nonebot import on_command, CommandSession
from nonebot import permission as perm

@on_command('say', permission=perm.GROUP_MEMBER, only_to_me=False)
async def say(session: CommandSession):
    chat_data = str(session.current_arg_text).strip()
    if chat_data == 'help':
        message = '#say 用户名 内容'
        await session.send(message)
    elif chat_data == '':
        message = '参数不全 获取帮助 #say help'
        await session.send(message)
    else:
        try:
            username = chat_data[:chat_data.find(' ')]
            text = chat_data[chat_data.find(' ')+1:]
            await rcon('tellraw @a {"extra":[{"text":"§a"},{"clickEvent":{"action":"suggest_command","value":"[QQ]' + username + '"},"text":"§f[QQ] ' + username + '§r: "},{"text":"§f"},{"text":"§f' + text + '"}],"text":""}')
        except Exception:
            message = '参数不全 获取帮助 #say help'
            await session.send(message)

async def rcon(_command: str) -> str:
    with MCRcon(rcon_setting['address'], rcon_setting['password'], rcon_setting['port']) as mcr:
        r = mcr.command(_command)
    return f'{r}'