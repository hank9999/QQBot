import re
from Libs.mcrcon import MCRcon
from pluginConfig.mcrcon_setting import rcon_setting


async def rcon(name, command) -> str:
    for k, v in rcon_setting.items():
        if k == name:
            with MCRcon(v['address'], v['password'], v['port']) as mcr:
                r = mcr.command(command)
            r = re.sub('§[0-9a-fk-or]', '', r, re.IGNORECASE)
            return r
        else:
            return '不存在该子服的RCON配置, 请检查子服名称'
