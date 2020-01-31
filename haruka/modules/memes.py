import random, re, string, io, asyncio
from PIL import Image
from io import BytesIO
import base64
from spongemock import spongemock
from zalgo_text import zalgo
from deeppyer import deepfry
import os
from pathlib import Path
import glob

from typing import Optional, List
from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from haruka import dispatcher, DEEPFRY_TOKEN
from haruka.modules.disable import DisableAbleCommandHandler, DisableAbleRegexHandler
from haruka.modules.translations.strings import tld

WIDE_MAP = dict((i, i + 0xFEE0) for i in range(0x21, 0x7F))
WIDE_MAP[0x20] = 0x3000

# D A N K modules by @deletescape vvv


@run_async
def owo(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    message = update.effective_message

    if message.reply_to_message:
        data = message.reply_to_message.text
    elif args:
        noreply = True
        data = message.text.split(None, 1)[1]
    else:
        data = tld(chat.id, "memes_no_message")

    faces = [
        '(・`ω´・)', ';;w;;', 'owo', 'UwU', '>w<', '^w^', '\(^o\) (/o^)/',
        '( ^ _ ^)∠☆', '(ô_ô)', '~:o', ';____;', '(*^*)', '(>_', '(♥_♥)',
        '*(^O^)*', '((+_+))'
    ]
    reply_text = re.sub(r'[rl]', "w", data)
    reply_text = re.sub(r'[ｒｌ]', "ｗ", data)
    reply_text = re.sub(r'[RL]', 'W', reply_text)
    reply_text = re.sub(r'[ＲＬ]', 'Ｗ', reply_text)
    reply_text = re.sub(r'n([aeiouａｅｉｏｕ])', r'ny\1', reply_text)
    reply_text = re.sub(r'ｎ([ａｅｉｏｕ])', r'ｎｙ\1', reply_text)
    reply_text = re.sub(r'N([aeiouAEIOU])', r'Ny\1', reply_text)
    reply_text = re.sub(r'Ｎ([ａｅｉｏｕＡＥＩＯＵ])', r'Ｎｙ\1', reply_text)
    reply_text = re.sub(r'\!+', ' ' + random.choice(faces), reply_text)
    reply_text = re.sub(r'！+', ' ' + random.choice(faces), reply_text)
    reply_text = reply_text.replace("ove", "uv")
    reply_text = reply_text.replace("ｏｖｅ", "ｕｖ")
    reply_text += ' ' + random.choice(faces)

    if noreply:
        message.reply_text(reply_text)
    else:
        message.reply_to_message.reply_text(reply_text)


@run_async
def stretch(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    message = update.effective_message

    if message.reply_to_message:
        data = message.reply_to_message.text
    elif args:
        noreply = True
        data = message.text.split(None, 1)[1]
    else:
        data = tld(chat.id, "memes_no_message")

    count = random.randint(3, 10)
    reply_text = re.sub(r'([aeiouAEIOUａｅｉｏｕＡＥＩＯＵ])', (r'\1' * count), data)

    if noreply:
        message.reply_text(reply_text)
    else:
        message.reply_to_message.reply_text(reply_text)


@run_async
def vapor(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    chat = update.effective_chat  # type: Optional[Chat]

    if message.reply_to_message:
        data = message.reply_to_message.text
    elif args:
        noreply = True
        data = message.text.split(None, 1)[1]
    else:
        data = tld(chat.id, "memes_no_message")

    reply_text = str(data).translate(WIDE_MAP)

    if noreply:
        message.reply_text(reply_text)
    else:
        message.reply_to_message.reply_text(reply_text)


# D A N K modules by @deletescape ^^^
# Less D A N K modules by @skittles9823 # holi fugg I did some maymays vvv


@run_async
def mafiatext(bot: Bot, update: Update):
    message = update.effective_message
    chat = update.effective_chat  # type: Optional[Chat]
    if message.reply_to_message:
        data = message.reply_to_message.text
    elif args:
        noreply = True
        data = message.text.split(None, 1)[1]
    else:
        data = tld(chat.id, "memes_no_message")

    if not Path('mafia.jpg').is_file():
        LOGGER.warning(
            "mafia.jpg not found! Mafia memes module is turned off!")
        return

    for mocked in glob.glob("mocked*"):
        os.remove(mocked)
    reply_text = spongemock.mock(data)

    randint = random.randint(1, 699)
    magick = """convert mafia.jpg -font Impact -pointsize 50 -size 1280x720 -stroke white -strokewidth 1 -fill black -background none -gravity north caption:"{}" -flatten mafiaed{}.jpg""".format(
        reply_text, randint)
    os.system(magick)
    with open('mafiaed{}.jpg'.format(randint), 'rb') as mockedphoto:
        if noreply:
            message.reply_photo(photo=mockedphoto,
                                reply=message.reply_to_message)
        else:
            message.reply_to_message.reply_photo(
                photo=mockedphoto, reply=message.reply_to_message)
    os.remove('mafiaed{}.jpg'.format(randint))


@run_async
def pidortext(bot: Bot, update: Update):
    message = update.effective_message
    chat = update.effective_chat  # type: Optional[Chat]
    if message.reply_to_message:
        data = message.reply_to_message.text
    elif args:
        noreply = True
        data = message.text.split(None, 1)[1]
    else:
        data = tld(chat.id, "memes_no_message")

    if not Path('4pda.jpg').is_file():
        LOGGER.warning("4pda.jpg not found! Pidor memes module is turned off!")
        return
    for mocked in glob.glob("mocked*"):
        os.remove(mocked)
    reply_text = spongemock.mock(data)

    randint = random.randint(1, 699)
    magick = """convert 4pda.jpg -font Impact -pointsize 50 -size 400x300 -stroke black -strokewidth 1 -fill white -background none -gravity north caption:"{}" -flatten 4pdaed{}.jpg""".format(
        reply_text, randint)
    os.system(magick)
    with open('4pdaed{}.jpg'.format(randint), 'rb') as mockedphoto:
        if noreply:
            message.reply_photo(photo=mockedphoto,
                                reply=message.reply_to_message)
        else:
            message.reply_to_message.reply_photo(
                photo=mockedphoto, reply=message.reply_to_message)
    os.remove('4pdaed{}.jpg'.format(randint))


@run_async
def kimtext(bot: Bot, update: Update):
    message = update.effective_message
    chat = update.effective_chat  # type: Optional[Chat]
    if message.reply_to_message:
        data = message.reply_to_message.text
    elif args:
        noreply = True
        data = message.text.split(None, 1)[1]
    else:
        data = tld(chat.id, "memes_no_message")

    if not Path('kim.jpg').is_file():
        LOGGER.warning("kim.jpg not found! Kim memes module is turned off!")
        return
    for mocked in glob.glob("mocked*"):
        os.remove(mocked)
    reply_text = spongemock.mock(data)

    randint = random.randint(1, 699)
    magick = """convert kim.jpg -font Impact -pointsize 50 -size 480x360 -stroke black -strokewidth 1 -fill white -background none -gravity north caption:"{}" -flatten kimed{}.jpg""".format(
        reply_text, randint)
    os.system(magick)
    with open('kimed{}.jpg'.format(randint), 'rb') as mockedphoto:
        if noreply:
            message.reply_photo(photo=mockedphoto,
                                reply=message.reply_to_message)
        else:
            message.reply_to_message.reply_photo(
                photo=mockedphoto, reply=message.reply_to_message)
    os.remove('kimed{}.jpg'.format(randint))


@run_async
def hitlertext(bot: Bot, update: Update):
    message = update.effective_message
    chat = update.effective_chat  # type: Optional[Chat]
    if message.reply_to_message:
        data = message.reply_to_message.text
    elif args:
        noreply = True
        data = message.text.split(None, 1)[1]
    else:
        data = tld(chat.id, "memes_no_message")

    if not Path('hitler.jpg').is_file():
        LOGGER.warning(
            "hitler.jpg not found! Hitler memes module is turned off!")
        return
    for mocked in glob.glob("hitlered*"):
        os.remove(mocked)
    reply_text = spongemock.mock(data)

    randint = random.randint(1, 699)
    magick = """convert hitler.jpg -font Impact -pointsize 50 -size 615x409 -stroke black -strokewidth 1 -fill white -background none -gravity north caption:"{}" -flatten hitlered{}.jpg""".format(
        reply_text, randint)
    os.system(magick)
    with open('hitlered{}.jpg'.format(randint), 'rb') as mockedphoto:
        if noreply:
            message.reply_photo(photo=mockedphoto,
                                reply=message.reply_to_message)
        else:
            message.reply_to_message.reply_photo(
                photo=mockedphoto, reply=message.reply_to_message)
    os.remove('hitlered{}.jpg'.format(randint))


@run_async
def spongemocktext(bot: Bot, update: Update):
    message = update.effective_message
    chat = update.effective_chat  # type: Optional[Chat]
    if message.reply_to_message:
        data = message.reply_to_message.text
    elif args:
        noreply = True
        data = message.text.split(None, 1)[1]
    else:
        data = tld(chat.id, "memes_no_message")

    if not Path('bob.jpg').is_file():
        LOGGER.warning(
            "bob.jpg not found! Spongemock memes module is turned off!")
        return
    for mocked in glob.glob("mocked*"):
        os.remove(mocked)
    reply_text = spongemock.mock(data)

    randint = random.randint(1, 699)
    magick = """convert bob.jpg -font Impact -pointsize 30 -size 512x300 -stroke black -strokewidth 1 -fill white -background none -gravity north caption:"{}" -flatten mocked{}.jpg""".format(
        reply_text, randint)
    os.system(magick)
    with open('mocked{}.jpg'.format(randint), 'rb') as mockedphoto:
        if noreply:
            message.reply_photo(photo=mockedphoto,
                                reply=message.reply_to_message)
        else:
            message.reply_to_message.reply_photo(
                photo=mockedphoto, reply=message.reply_to_message)
    os.remove('mocked{}.jpg'.format(randint))


@run_async
def zalgotext(bot: Bot, update: Update):
    message = update.effective_message
    chat = update.effective_chat  # type: Optional[Chat]
    if message.reply_to_message:
        data = message.reply_to_message.text
    elif args:
        noreply = True
        data = message.text.split(None, 1)[1]
    else:
        data = tld(chat.id, "memes_no_message")

    reply_text = zalgo.zalgo().zalgofy(data)
    if noreply:
        message.reply_text(reply_text)
    else:
        message.reply_to_message.reply_text(reply_text)


# Less D A N K modules by @skittles9823 # holi fugg I did some maymays ^^^
# shitty maymay modules made by @divadsn vvv


@run_async
def deepfryer(bot: Bot, update: Update):
    message = update.effective_message
    chat = update.effective_chat  # type: Optional[Chat]
    if message.reply_to_message:
        data = message.reply_to_message.photo
        data2 = message.reply_to_message.sticker
    else:
        data = []
        data2 = []

    # check if message does contain media and cancel when not
    if not data and not data2:
        message.reply_text(tld(chat.id, "memes_deepfry_nothing"))
        return

    # download last photo (highres) as byte array
    if data:
        photodata = data[len(data) - 1].get_file().download_as_bytearray()
        image = Image.open(io.BytesIO(photodata))
    elif data2:
        sticker = bot.get_file(data2.file_id)
        sticker.download('sticker.png')
        image = Image.open("sticker.png")

    # the following needs to be executed async (because dumb lib)
    loop = asyncio.new_event_loop()
    loop.run_until_complete(
        process_deepfry(image, message.reply_to_message, bot))
    loop.close()


async def process_deepfry(image: Image, reply: Message, bot: Bot):
    # DEEPFRY IT
    image = await deepfry(img=image,
                          token=DEEPFRY_TOKEN,
                          url_base='westeurope')

    bio = BytesIO()
    bio.name = 'image.jpeg'
    image.save(bio, 'JPEG')

    # send it back
    bio.seek(0)
    reply.reply_photo(bio)
    if Path("sticker.png").is_file():
        os.remove("sticker.png")


# shitty maymay modules made by @divadsn ^^^


@run_async
def shout(bot: Bot, update: Update, args):
    chat = update.effective_chat  # type: Optional[Chat]
    if len(args) == 0:
        update.effective_message.reply_text(tld(chat.id, "memes_shout_notext"))
        return

    if message.reply_to_message:
        data = message.reply_to_message.text
    elif args:
        noreply = True
        data = " ".join(args)
    else:
        data = tld(chat.id, "memes_no_message")

    msg = "```"
    result = []
    result.append(' '.join([s for s in data]))
    for pos, symbol in enumerate(data[1:]):
        result.append(symbol + ' ' + '  ' * pos + symbol)
    result = list("\n".join(result))
    result[0] = data[0]
    result = "".join(result)
    msg = "```\n" + result + "```"
    return update.effective_message.reply_text(msg, parse_mode="MARKDOWN")


__help__ = True

OWO_HANDLER = DisableAbleCommandHandler("owo", owo, admin_ok=True)
STRETCH_HANDLER = DisableAbleCommandHandler("stretch", stretch)
VAPOR_HANDLER = DisableAbleCommandHandler("vapor",
                                          vapor,
                                          pass_args=True,
                                          admin_ok=True)
MOCK_HANDLER = DisableAbleCommandHandler("mock", spongemocktext, admin_ok=True)
KIM_HANDLER = DisableAbleCommandHandler("kim", kimtext, admin_ok=True)
MAFIA_HANDLER = DisableAbleCommandHandler("mafia", mafiatext, admin_ok=True)
PIDOR_HANDLER = DisableAbleCommandHandler("pidor", pidortext, admin_ok=True)
HITLER_HANDLER = DisableAbleCommandHandler("hitler", hitlertext, admin_ok=True)
ZALGO_HANDLER = DisableAbleCommandHandler("zalgofy", zalgotext)
DEEPFRY_HANDLER = DisableAbleCommandHandler("deepfry",
                                            deepfryer,
                                            admin_ok=True)
SHOUT_HANDLER = DisableAbleCommandHandler("shout", shout, pass_args=True)

dispatcher.add_handler(MAFIA_HANDLER)
dispatcher.add_handler(PIDOR_HANDLER)
dispatcher.add_handler(SHOUT_HANDLER)
dispatcher.add_handler(OWO_HANDLER)
dispatcher.add_handler(STRETCH_HANDLER)
dispatcher.add_handler(VAPOR_HANDLER)
dispatcher.add_handler(MOCK_HANDLER)
dispatcher.add_handler(ZALGO_HANDLER)
dispatcher.add_handler(DEEPFRY_HANDLER)
dispatcher.add_handler(KIM_HANDLER)
dispatcher.add_handler(HITLER_HANDLER)
