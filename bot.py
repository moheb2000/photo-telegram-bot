from uuid import uuid4 # for picture's unique name
from PIL import Image # for changing image with pillow module
from os import remove # for remove risult image

### import from python-telegram-bot-module begin ###

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.chataction import ChatAction
from telegram import PhotoSize

### import from python-telegram-bot-module end ###

TOKEN = '1179333777:AAH-HWef2NLcvRQtZUdLruw0Hy4oRQQLg-0'

update = Updater(TOKEN, use_context=True)
dispatcher = update.dispatcher

# function start run when user enter /start command in telegram
def start(update, context):
    chat_id = update.message.chat_id

    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    context.bot.send_message(chat_id, 'سلام به همه دوستای خوبم😁😁\nخوشحالم از این بات استفاده می کنید😍🥰😍\nاین ربات یه کار ساده انجام میده. عکس رو از شما میگیره و روی اون یه کاور میزاره و دوباره براتون ارسال می کنه☺\nفقط کافیه عکسو براش ارسال کنید😉🙃')


# function send_image run when user send an image for robot
def send_image(update, context):
    chat_id = update.message.chat_id
    
    # generate image name
    filename = str(uuid4()) + '.jpg'

    # download image from telegram server and save it in download directory
    myfile = context.bot.get_file(update.message.photo[-1].file_id).download('./download/' + filename)

    ### pillow code for robot back-end begin ###

    photo1 = Image.open(myfile)
    photo2 = Image.open('cover.png')

    # merge to images together
    photo1.paste(photo2, (0, 0), photo2)

    # save result image in upload directory
    photo1.save('./upload/' + filename, 'JPEG')

    ### pillow code for robot back-end finish ###


    # open new image with python
    new_img = open('./upload/' + filename, 'rb')

    # send output to client
    context.bot.send_chat_action(chat_id, ChatAction.UPLOAD_PHOTO)
    context.bot.send_photo(chat_id, new_img)
    new_img.close()


# add handlers to robot
start_command = CommandHandler('start', start)
image_message_handler = MessageHandler(Filters.photo, send_image)


# dispatch handlers
dispatcher.add_handler(start_command)
dispatcher.add_handler(image_message_handler)


# run robot in telegram
update.start_polling()

