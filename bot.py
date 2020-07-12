#!/usr/bin/python

from telethon import TelegramClient, events, errors
import logging
import socks
import conf
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

api_id = conf.API_ID
api_hash = conf.API_HASH
chats = conf.CHANNELS_TO_GET_UPDATES_FROM
session_file = 'anon'


if conf.AUTHENTICATION:
    sockProxy = {
        "proxy_type": socks.SOCKS5,
        "addr": conf.SOCKS5_SERVER,
        "port": conf.SOCKS5_PORT,
        "rdns": True,
        "username": conf.USERNAME,
        "password": conf.PASSWORD
    }

if conf.PROXY:
    if conf.AUTHENTICATION:
        if conf.USERNAME is not None and conf.PASSWORD is not None:
            client = TelegramClient(session_file, api_id, api_hash, proxy=sockProxy)
    elif not conf.AUTHENTICATION:
        client = TelegramClient(session_file, api_id, api_hash, proxy=(socks.SOCKS5, conf.SOCKS5_SERVER, conf.SOCKS5_PORT))
else:
    client = TelegramClient(session_file, api_id, api_hash)

# client = TelegramClient(session_file, api_id, api_hash)

chats = conf.CHANNELS_TO_GET_UPDATES_FROM


@client.on(events.NewMessage(chats, blacklist_chats=False))
async def newMessageHandler(msg):
    await client.send_message(conf.OWN_CHANNEL_ID, msg.message)


try:
    client.start()
    print("\n-------------------------\nMessage Forward bot is up!\n-------------------------\n")
    print("To run in the background type 'nohup python /path/to/app &' command. Thanks!\n")
    client.run_until_disconnected()
except KeyboardInterrupt:
    print("\nQuiting bot!")
except errors.rpcerrorlist.ApiIdInvalidError:
    print("Invalid API_ID/API_HASH")
