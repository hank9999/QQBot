from nonebot import on_command, CommandSession
from nonebot import permission as perm
from Libs.getServerStatus import getStatus


@on_command('status', aliases=('服务器状态', '状态', 'list'), permission=perm.GROUP_MEMBER, only_to_me=False)
async def statusCommand(session: CommandSession):
    message = await getStatus()
    await session.send(message)


