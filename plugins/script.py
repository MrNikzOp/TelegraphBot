from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

  START_TEXT = """
  Heyy {} !!

I am Telegraph bot. I can upload 
media file on Telegra.ph. Maximum 
file size limit is 5Mb.
"""
  HELP_TEXT = """
  **Send Me a Picture Or Video Under 5Mb. I Will Try To Post it On** telegra.ph
  """
  BOTCHANNEL_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🎉 Bot Channel', url='https://t.me/+968jk8GzycIxYTY1')
        ],[
        InlineKeyboardButton('🤖 Source', url='https://github.com/MrNikzOp/TelegraphBot')  
        ]]
  )
