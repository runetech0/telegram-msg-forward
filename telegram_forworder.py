#!/usr/bin/python

from telethon import TelegramClient,events, errors
import logging
import socks
import telegram_conf as conf
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

api_id = conf.API_ID
api_hash = conf.API_HASH
chats = conf.CHANNELS_TO_GET_UPDATES_FROM 


if conf.PROXY:
    if conf.AUTHENTICATION:
        if conf.USERNAME != None and conf.PASSWORD != None:
            client = TelegramClient('anon', api_id, api_hash, proxy=(socks.SOCKS5, conf.SOCKS5_SERVER, conf.SOCKS5_PORT, conf.USERNAME, conf.PASSWORD))
    elif not conf.AUTHENTICATION:
        client = TelegramClient('anon', api_id, api_hash, proxy=(socks.SOCKS5, conf.SOCKS5_SERVER, conf.SOCKS5_PORT))
else:
    client = TelegramClient('anon', api_id, api_hash) 



@client.on(events.NewMessage(chats, blacklist_chats=False))
async def newMessageHandler(msg):
    await client.send_message(conf.OWN_CHANNEL_ID, msg.message)




try:
    client.start()
    print("\n-------------------------\nMessage Forwarder is up!\n-------------------------\n")
    print("To run in the background type 'nohup python /path/to/app &' command. Thanks!\n")
    client.run_until_disconnected()
except KeyboardInterrupt:
    print("\nQuiting bot!")
except errors.rpcerrorlist.ApiIdInvalidError:
    print("Invalid API_ID/API_HASH")

