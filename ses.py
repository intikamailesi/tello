from telegram import Update,update
from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters 
# Импорт библиотеки модулей преобразования текстовых сообщений в голосовые 
from pyrogram import Client
import pyttsx3
import subprocess

engine=pyttsx3.init()
engine.setProperty(
    'voice',
    'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\
    TTS_MS_RU-RU_IRINA_11.0'
    ) 
      
'''
DOCSTRING: With cross-platform program"ffmpeg",
    command "subprocess.run([ffmpeg ...])" this function
    convertsthe mp3 file format to ogg, for correct transmission
    to TelegramBot.
INPUT:mp3_file(mp3).
OUTPUT:out_file(ogg).
''' 
  
def text_to_file(text):    
    mp3_file=f"data/temp.mp3"
    out_file=f"data/temp.ogg"
    engine.save_to_file(text,mp3_file)
    engine.runAndWait()
    subprocess.run(["ffmpeg",'-i',mp3_file ,'-acodec','libopus',out_file ,'-y'])
    return out_file

TOKEN = "5797164515:AAG1PBBNhpLFqwO0Zn_UBYWSLvqaOpvyZhA"
api_id = "6058190"
api_hash = "05902397a996c693f809f5cc24106fae"
Client = api_id, api_hash, TOKEN

@Client.on_message(filters.command(["sesecevir"], ["/", "."]))
def reply (update,context):
    text=update.message.text
    if text==text[::-1]:
        sounds_sign=text_to_file(text+" А Вы знали?,что это-палиндром!")    
    else:
        sounds_sign=text_to_file(text)
# Вызываем голосовое сообщение из текста пользователя.        
    update.message.reply_voice(voice=open(sounds_sign,'rb'))

Client.run()
