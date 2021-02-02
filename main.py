from dhooks import Webhook
from Reddit_ChatBot_Python import ChatBot, RedditAuthentication


dc_webhook_url = ""

reddit_bot_authentication = RedditAuthentication.PasswordAuth(reddit_username="", reddit_password="", twofa="")
chatbot = ChatBot(print_chat=True, store_session=True, authentication=reddit_bot_authentication)

hook = Webhook(dc_webhook_url)


@chatbot.after_message_hook(frame_type='MESG')
def send2discord(resp):
    hook.send(f"{resp.user.name}@{chatbot.get_chatroom_name_id_pairs().get(resp.channel_url)}: {resp.message}")
