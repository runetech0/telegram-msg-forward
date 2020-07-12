#!/usr/bin/python

from telethon import TelegramClient, events, errors
# import logging
import conf

# logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
# level=logging.WARNING)

api_id = conf.API_ID
api_hash = conf.API_HASH
chats = conf.CHANNELS_TO_GET_UPDATES_FROM
session_file = 'anon'


client = TelegramClient(session_file, api_id, api_hash)

chats = conf.CHANNELS_TO_GET_UPDATES_FROM


@client.on(events.NewMessage(chats, blacklist_chats=False))
async def newMessageHandler(msg):
    await client.send_message(conf.OWN_CHANNEL_ID, msg.message)


try:
    client.start()
    print("-------------------------\nMessage Forward bot is up!\n-------------------------\n")
    print("[+] To run in the background type 'nohup python /path/to/app &' command. Thanks!\n")
    client.run_until_disconnected()
except KeyboardInterrupt:
    print("[+] Quiting bot!")
except errors.rpcerrorlist.ApiIdInvalidError:
    print("[+] Invalid API_ID/API_HASH")
