from mcstatus import MinecraftServer
from pluginConfig.status_setting import serverList


def createJson(ip, port):
    server = MinecraftServer(ip, port)
    data = {'online': False}
    # Build data with responses and quit on exception
    try:
        status_res = server.status(retries=1)
        data['online'] = True
        data['version'] = status_res.version.name
        data['protocol'] = status_res.version.protocol
        data['motd'] = status_res.description
        data['player_count'] = status_res.players.online
        data['player_max'] = status_res.players.max
        data['players'] = []
        if status_res.players.sample is not None:
            data['players'] = [{'name': player.name, 'id': player.id} for player in status_res.players.sample]
    except Exception:
        pass
    return data


def createBungeeJson(ip, port):
    server = MinecraftServer(ip, port)
    data = {'online': False}
    # Build data with responses and quit on exception
    try:
        status_res = server.status(retries=1)
        data['online'] = True
        data['version'] = status_res.version.name
        data['protocol'] = status_res.version.protocol
        data['motd'] = status_res.description
        data['player_count'] = status_res.players.online
        data['player_max'] = status_res.players.max
    except Exception:
        pass
    return data


def playerList(players):
    plist = ''
    for i in players:
        plist += i['name'] + ', '
    plist = plist[:len(plist) - 2]
    if plist == '':
        return '没有在线玩家'
    return plist


async def getStatus() -> str:
    r = ''
    for k, v in serverList.items():
        if v['type'] == 'bungee':
            s = createBungeeJson(v['ip'], v['port'])
            if s['online']:
                r += ('{} 版本: {} 人数: {}/{}\n'.format(k, s['version'], s['player_count'], s['player_max']))
            else:
                r += ('{} 不在线\n'.format(k))
        else:
            s = createJson(v['ip'], v['port'])
            if s['online']:
                r += ('{} 版本: {} 人数: {}/{} 玩家: {}\n'.format(
                    k,
                    s['version'],
                    s['player_count'],
                    s['player_max'],
                    playerList(s['players'])
                ))
            else:
                r += ('{} 不在线\n'.format(k))
    return r
