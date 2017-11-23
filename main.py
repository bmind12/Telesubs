from telethon import TelegramClient

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'
phone = '+420774134850'

client = TelegramClient('session_name', api_id, api_hash)
client.connect()

# If you already have a previous 'session_name.session' file, skip this.
client.sign_in(phone=phone)
me = client.sign_in(code=77777)  # Put whatever code you received here.