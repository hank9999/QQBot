from nonebot import on_command, CommandSession
from nonebot import permission as perm


@on_command('help', aliases='帮助', permission=perm.GROUP_MEMBER, only_to_me=False)
async def helpCommand(session: CommandSession):
    await session.send(
        '帮助: \n'
        '#mute help 查看禁言帮助\n'
        '#unmute help 查看解除禁言帮助\n'
        '#say help 查看消息帮助\n'
        '#list 列出当前子服信息\n'
        '#rconlist 列出所有具有RCON子服名称'
    )