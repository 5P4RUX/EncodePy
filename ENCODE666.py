import os
import base64
import marshal
import random
import zlib
import telebot
from telebot import types
import pyfiglet

B = '\033[1;32m'
A = '\033[1;90m'
text = pyfiglet.figlet_format("EncodePy", font="slant")
print(f'{B}{text[:-4]}{text[-4:]}')
sa = input(f'\n{A}⌯ENTER BOT TOKEN : ')
bot = telebot.TeleBot(sa)
print(f'{B}BOT ONLINE BY SPARUX-666...')


#-----------------------[protokol]----------------------#
zlb = lambda in_: zlib.compress(in_)
b16 = lambda in_: base64.b16encode(in_)
b32 = lambda in_: base64.b32encode(in_)
b64 = lambda in_: base64.b64encode(in_)
mar = lambda in_: marshal.dumps(compile(in_, 'module', 'exec'))

#-----------------------[BAŞLA]----------------------#
@bot.message_handler(commands=['start'])
def BASLA(message):            
    s1 = types.InlineKeyboardButton(text="Marshal", callback_data='marshal')
    s2 = types.InlineKeyboardButton(text="Base64", callback_data='base64')
    s3 = types.InlineKeyboardButton(text="Lambda", callback_data='lambda')
    s4 = types.InlineKeyboardButton(text="Zlib", callback_data='zlib2')
    s5 = types.InlineKeyboardButton(text="Marshal + Zlib", callback_data='marshal_zlib')    
    s6 = types.InlineKeyboardButton(text="Zlib + Base16", callback_data='zlib_base16')
    s7 = types.InlineKeyboardButton(text="Base32 + Zlib", callback_data='base32_zlib')
    s8 = types.InlineKeyboardButton(text="Marshall + Zlib + Base16", callback_data='marshall_zlib_base16')
    s9 = types.InlineKeyboardButton(text="Marshall + Zlib + Base64", callback_data='marshall_zlib_base64')     
    Keyy = types.InlineKeyboardMarkup()
    Keyy.row_width = 2
    Keyy.add(s1, s2, s3, s4, s5, s6, s7, s8, s9)
    bot.send_message(message.chat.id, text=f"Welcome! Select the encryption type.", parse_mode="markdown", reply_markup=Keyy)

#-----------------------[şifreleme]----------------------#    
@bot.callback_query_handler(func=lambda call: True)
def encode3(call):
    if call.data == "marshal":
        encode2(call.message, "marshal")
    elif call.data == "base64":
        encode2(call.message, "base64")
    elif call.data == "lambda":
        encode2(call.message, "lambda")
    elif call.data == "zlib2":
        encode2(call.message, "zlib2")
    elif call.data == "zlib_base16":
        encode2(call.message, "zlib_base16")
    elif call.data == "marshal_zlib":
        encode2(call.message, "marshal_zlib")
    elif call.data == "base32_zlib":
        encode2(call.message, "base32_zlib")
    elif call.data == "marshall_zlib_base16":
        encode2(call.message, "marshall_zlib_base16")
    elif call.data == "marshall_zlib_base64":
        encode2(call.message, "marshall_zlib_base64")

#-----------------------[DOSYA GÖNDER]----------------------#
def encode2(message, call):
    bot.send_message(message.chat.id, text=f"Please send the file to be encrypted. [{call}]")
    @bot.message_handler(content_types=['document'])
    def save(message):
        file_input = bot.download_file(bot.get_file(message.document.file_id).file_path)
        us = str("".join(random.choice('1234567890') for i in range(4)))
        file_name = f"{call}-{us}.py"
        with open(file_name, 'wb') as f:
            f.write(file_input)
        s3 = encode(call, file_name)
        with open(file_name, 'w') as f:
            f.write(s3)
        file_document = open(file_name, 'rb')
        bot.send_document(message.chat.id, file_document)
        os.system(f"rm -f {file_name}")

#-----------------------[kod]----------------------#        
def encode(call, file_name):
    if call == "base64":
        s3 = b64(open(file_name, "r").read().encode('utf8'))[::-1]
        return (f"_ = lambda __ : __import__('base64').b64decode(__[::-1]);exec((_)({s3}))")

    elif call == "lambda":
        s3 = repr(zlib.compress(open(file_name, "r").read().encode('utf-8')))        
        return (f"import zlib\nexec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(_____),'module','exec'))({s3},compile))")

    elif call == "marshal":
        s3 = marshal.dumps(compile(open(file_name, "r").read(), 'module', 'exec'))
        return (f"import marshal\nexec(marshal.loads({s3}))")

    elif call == "zlib2":
        s3 = str(base64.b64encode(zlib.compress(marshal.dumps(compile(open(file_name, "r").read(), "ru", 'exec')))))
        return (f"import base64\nimport zlib\nimport marshal\nexec(marshal.loads(zlib.decompress(base64.b64decode({s3}))))")

    elif call == "zlib_base16":
        s3 = b16(zlb(open(file_name, "r").read().encode('utf8')))[::-1]
        return (f"_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));exec((_)({s3}))")

    elif call == "base32_zlib":
        s3 = b32(zlb(open(file_name, "r").read().encode('utf8')))[::-1]
        return (f"_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1])); exec((_)({s3}))")

    elif call == "marshall_zlib_base16":
        s3 = b16(zlb(mar(open(file_name, "r").read().encode('utf8'))))[::-1]
        return (f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));exec((_)({s3}))")

    elif call == "marshall_zlib_base64":
        s3 = b64(zlb(mar(open(file_name, "r").read().encode('utf8'))))[::-1]
        return (f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)({s3}))")

    elif call == "marshal_zlib":
        s3 = zlb(mar(open(file_name, "r").read().encode('utf8')))[::-1]
        return (f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));exec((_)({s3}))")

bot.polling(True)
  
