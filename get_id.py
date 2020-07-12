
from telethon import TelegramClient, events, errors
# import logging
import conf
# logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
# level=logging.WARNING)


api_id = conf.API_ID
api_hash = conf.API_HASH
session_file = 'bot'


client = TelegramClient(session_file, api_id, api_hash)

try:
    while True:
        print("[+] Please Select the channel type using number. CTRL+c : quit.\n[1] Public Channel\n[2] Private/Public Group + Private Channel")
        s = input("[+] Enter 1 or 2: ")
        if int(s) == (1):
            public = True
            guideMsg = "[+] Goto the public channel and forward a message from that channel.\n"
            break
        elif int(s) == 2:
            public = False
            guideMsg = "[+] Goto the channel you want to get id for and send a message!\n"
            break
        else:
            print("[-] Invalid selection. Please Try again!\n")
            continue
except KeyboardInterrupt:
    print("\nQuiting ...\n")
    quit()


@client.on(events.NewMessage())
async def newMessageHandler(msg):
    if public:
        try:
            if msg.fwd_from.channel_id:
                print("-------------------------------------------------------------")
                print("[+] Forwarded message is: {msg.raw_text}")
                print("\n[+] Chat id for public channel is: {msg.fwd_from.channel_id}\n")
                print("-------------------------------------------------------------\n")
        except AttributeError:
            pass
    else:
        try:
            if msg.chat_id:
                print("---------------------------------------------------")
                print(f"[+] Sent message is: {msg.raw_text}")
                print(f"\n[+] The chat id for the channel is: {msg.chat_id}")
                print("--------------------------------------------------\n")
        except AttributeError:
            pass


try:
    client.start()
    print(guideMsg)
    client.run_until_disconnected()
except errors.rpcerrorlist.ApiIdInvalidError:
    print("[-] Invalid API_ID/API_HASH")
except KeyboardInterrupt:
    print("[+] \nQuiting ...")
