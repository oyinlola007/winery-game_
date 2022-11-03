import webcolors, discord
from datetime import datetime
from dateutil.relativedelta import relativedelta

import cogs.config as config

def getColour(colour):
    return int("0x" + webcolors.name_to_hex(colour).strip("#"), 16)

def generate_embed(text, name, image_link = None, title = None):
    if title != None:
        embed=discord.Embed(color=getColour("purple"), description=text, title=title)
    else:
        embed=discord.Embed(color=getColour("purple"), description=text)

    embed.set_footer(text=config.FOOTER_TEXT.format(name))

    if image_link != None:
        embed.set_image(url=image_link)

    return embed

def get_time_after(checkpoint, duration):
    date_int = datetime.strptime(checkpoint, config.DATE_FORMAT)
    date_int_after = date_int + relativedelta(minutes=int(duration))
    return date_int_after.strftime(config.DATE_FORMAT)

def get_percentage_time_completed(checkpoint, duration):
    time_done = (datetime.now() - datetime.strptime(checkpoint, config.DATE_FORMAT)).seconds
    percentage = time_done/(int(duration)*60)
    return percentage

def get_checkpoint():
    return datetime.now().strftime(config.DATE_FORMAT)

def is_elapsed(time_stamp):
    if datetime.now() > datetime.strptime(time_stamp, config.DATE_FORMAT):
        return True
    else:
        return False

def get_time_left(time_stamp):
    time_left = (datetime.strptime(time_stamp, config.DATE_FORMAT) - datetime.now()).seconds
    return "{:02}:{:02}:{:02}".format(time_left//3600, time_left%3600//60, time_left%60)

def convert_min_to_time(min):
    return "{:02}:{:02}:00".format(int(min)//60, int(min)%60)

def convert_to_thousands(n):
    try:
        n = int(n)
        return f'{n:,}'
    except:
        return n

intervals = (
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
)

def get_days_left(time_stamp):
    seconds = int((datetime.strptime(time_stamp, config.DATE_FORMAT) - datetime.now()).total_seconds())
    granularity = 4
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])