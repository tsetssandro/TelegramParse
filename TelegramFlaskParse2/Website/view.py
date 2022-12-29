from flask import request, render_template, Blueprint, flash
from telethon import TelegramClient, sync
from . import app
import asyncio
import time

api_id = 27752867
api_hash = '08b3674aa7d4061fd64103a2d611ef89'
phone_number = '+995557335435'


views = Blueprint("views",__name__)

@views.route("/", methods=["POST","GET"])

def homepage():
    if request.method == "POST":
        data = request.form
        password = request.form.get("password")
                    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    client = TelegramClient(None, api_id, api_hash, loop=loop)

    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        try:
            code = input('Enter the code: ')
        except EOFError:
            print("hello")

    client.sign_in(phone_number, code)

    chats = client.get_dialogs()

    for chat in chats:
        print(f'{chat.name} ({chat.id})')



    return render_template("main.html", chats = chats)

