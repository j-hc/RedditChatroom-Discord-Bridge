from dhooks import Webhook
from Reddit_ChatBot_Python.ChatBot import ChatBot


def send2discord(resp):
    if resp.type_f == "MESG":
        to_send = f"{resp.user.name}: {resp.message}"
        hook.send(to_send)


if __name__ == "__main__":
    sub_channels = ["Turkey"]
    dc_webhook_url = ""
    reddit_api_token = ""

    hook = Webhook(dc_webhook_url)
    chatbot = ChatBot(reddit_api_token=reddit_api_token, sub_channels=sub_channels, print_chat=True, store_session=True)
    websock = chatbot.WebSocketClient

    websock.add_after_message_hook(send2discord)

    while True:
        try:
            websock.run_4ever()
        except:
            continue
