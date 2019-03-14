import datetime
import os

from aiotg import Bot, Chat

bot = Bot(api_token=os.getenv('TOKEN', ''))

base_phrase = "Do you ask me about deploy to prod?\n"


@bot.command(r".*")
def echo(chat: Chat, match):
    date = datetime.date.today()
    day_x = datetime.date(year=2019, month=3, day=14,)
    if date == day_x:
        return chat.reply("NO, YOU CAN'T TODAY!")
    else:
        return chat.reply("Yes, ofcourse, if tests are good and you want to.")


bot.run()
