import json
import dateti
import os 
import telebot
from telebot import apihelper
apihelper.SESSION_TIMEOUT = 80
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


bot = telebot.TeleBot('')

@bot.message_handler(commands=['help','start'])
def send_welcome(message):
    bot.reply_to(message,'hello men what me can help you')

@bot.message_handler(commands=['video'])
def send_video(message):
    print('send musik.....')
    video = open('test.mp3','rb')
    bot.send_document(message.chat.id,video,caption='ini bos')
    video.close()
    print('sukses')

@bot.message_handler(commands=['test'])
def hello(message):
    bot.reply_to(message,'yo men')

@bot.message_handler(commands=['inline'])
def inline_buttons(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("Google", url="https://www.google.com"),
        InlineKeyboardButton("Klik Saya", callback_data="button_click")
    )
    bot.send_message(message.chat.id, "Pilih tombol:", reply_markup=markup)

@bot.message_handler(commands=['keyboard'])
def reply_keyboard(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        KeyboardButton("📷 Kirim Foto"),
        KeyboardButton("📄 Kirim Dokumen")
    )
    markup.row(
        KeyboardButton("🎵 Kirim Audio"),
        KeyboardButton("❌ Hapus Keyboard")
    )
    bot.send_message(message.chat.id, "Gunakan tombol berikut:", reply_markup=markup)
bot.polling()