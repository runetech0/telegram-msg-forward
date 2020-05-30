
from telethon import TelegramClient,events, errors, utils
import logging
import socks
import telegram_conf as conf
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


api_id = conf.API_ID
api_hash = conf.API_HASH



if conf.PROXY:
    print("[+] Proxy Enabled!")
    client = TelegramClient('anon', api_id, api_hash, proxy=(socks.SOCKS5, conf.SOCKS5_SERVER, conf.SOCKS5_PORT))
else:
    print("[+] Proxy Disabled!")
    client = TelegramClient('anon', api_id, api_hash)



try:
    while True:
        print(f"[+] Please Select the channel type using number. CTRL+c : quit.\n[1] Public\n[2] Private")
        s = input("Enter 1 or 2: ")
        if int(s) == (1):
            public = True
            guideMsg = "[+] Goto the public channel and forward a message from that channel.\n"
            break
        elif int(s) == 2:
            public = False
            guideMsg = "[+] Goto the channel you want to get id for and send a message!\n"
            break
        else:
            print("[-]Invalid selection. Please Try again!\n")
            continue
except KeyboardInterrupt:
    print("\nQuiting ...\n")
    quit()




@client.on(events.NewMessage())
async def newMessageHandler(msg):
    if public:
        print(f"Chat id for public channel is: {msg.fwd_from.channel_id}\n")
    else:
        print(f"Sent message is: {msg.raw_text}\nThe chat id for the channel is: {msg.chat_id}\n---------------------------------------\n")





try:
    client.start()
    print(guideMsg)
    client.run_until_disconnected()
except errors.rpcerrorlist.ApiIdInvalidError:
    print("Invalid API_ID/API_HASH")
except KeyboardInterrupt:
    print(f"\nQuiting ...")
