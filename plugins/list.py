from mcrcon import MCRcon
from mcrcon_setting import rcon_setting
import re
from nonebot import on_command, CommandSession
from nonebot import permission as perm

@on_command('list', permission=perm.GROUP_MEMBER, only_to_me=False)
async def _list(session: CommandSession):
    result = await rcon('who')
    await session.send(result)


async def rcon(_command: str) -> str:
    with MCRcon(rcon_setting['address'], rcon_setting['password'], rcon_setting['port']) as mcr:
        r = mcr.command(_command)
    r = re.sub('§[0-9]', '', r)
    r = re.sub('§[a-f]', '', r)
    r = re.sub('§[k-o]', '', r)
    r = r.replace('§r', '')
    return f'{r}'