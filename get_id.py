from telethon import TelegramClient,events, errors
import logging
import socks
import telegram_conf as conf
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


# Use your own values from my.telegram.org
api_id = conf.API_ID
api_hash = conf.API_HASH



client = TelegramClient('anon', api_id, api_hash)


@client.on(events.NewMessage())
async def newMessageHandler(msg):
    print(f"Sent message is: {msg.raw_text}\nThe chat id for the channel is: {msg.chat_id}\n---------------------------------------\n")
    
try:
    client.start()
    print("[+] Goto the channel you want to get id for and send a message!\n")
    client.run_until_disconnected()
except errors.rpcerrorlist.ApiIdInvalidError:
    print("Invalid API_ID/API_HASH")
except KeyboardInterrupt:
    print(f"\nQuiting ...")
