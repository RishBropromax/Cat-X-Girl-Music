from CatXGirl import app

from CatXGirl_Music.commands import *

@app.on_message(command("#Repo"))

async def plug(_, message):

    CatXGirl = await message.reply_text(text="Hello I am CatXGirl Bot. Im  Powerfull And Fast Telegram Bot.. [Cat X Girl Music](https://github.com/RishBropromax/Cat-X-Girl-Music) "  

 )

    ImRishmika = """

I'm a Vc Player And Group manager Bot.

@CatXGirl_Bot

    """

    await CatXGirl.edit_text(ImRishmika)
    
@app.on_message(command("#Ower"))

async def plug(_, message):

    CatXGirl = await message.reply_text(text="Hello I am CatXGirl Music Bot. Im  Powerfull And Fast Telegram Bot.. [Cat X Girl Music](https://github.com/RishBropromax/Cat-X-Girl-Music) \n\n My Devoloper @ImRishmika \n\n Start [Rishmika Sandanu Assistant Bot](t.me/ImRishmika_Bot) "  

 )

    ImRishmika = """

I'm a Vc Player And Group manager Bot.

@CatXGirl_Bot

    """

    await CatXGirl.edit_text(ImRishmika)


__HELP__ = """  

#Repo - Github Repo
Ower - Ower On This Repo

"""
