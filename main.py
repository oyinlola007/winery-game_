import discord, asyncio, warnings
from tabulate import tabulate

import cogs.config as config
import cogs.db as db
import cogs.utils as utils
import cogs.strings as strings

warnings.filterwarnings("ignore", category=DeprecationWarning)
intents = discord.Intents.all()
client = discord.Client(intents=intents)

db.initializeDB()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if not message.author.bot:
        if message.content == "!startWinery":
            try:
                db.insert_player_details(message.author.id)
                await message.channel.send(embed=utils.generate_embed(strings.WELCOME_TO_WINERY.format(message.content), message.author.name, config.LINK_STARTWINERY))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.WINERY_EXISTS, message.author.name))

        elif db.get_tracker(message.author.id) != "":
            if db.get_tracker(message.author.id) == "winery_name":
                db.update_winery_name(message.author.id, message.content)
                db.update_tracker(message.author.id, "grape_variety")
                await message.channel.send(embed=utils.generate_embed(strings.WINERY_NAME_ENTERED.format(message.content), message.author.name, config.LINK_STARTWINERY))

            elif db.get_tracker(message.author.id) == "grape_variety":
                if message.content in ["Barbera", "Chardonnay", "Nebbiolo", "Arneis", "Dolcetto", "Cortese"]:
                    db.update_grape_variety(message.author.id, message.content)
                    db.update_tracker(message.author.id, "")
                    await message.channel.send(embed=utils.generate_embed(strings.GRAPE_VARIETY_ENTERED.format(message.content), message.author.name, config.LINK_STARTWINERY))
                else:
                    await message.channel.send(embed=utils.generate_embed(strings.WRONG_GRAPE_SELECTION, message.author.name))

        elif message.content == "!harvest":
            try:
                current_process = db.get_current_process(message.author.id)
                if current_process == "harvest":
                    await message.channel.send(embed=utils.generate_embed(strings.HARVEST_IN_PROGRESS, message.author.name, config.LINK_HARVEST))
                elif current_process == "":
                    db.update_current_process(message.author.id, "harvest", utils.get_checkpoint())
                    await message.channel.send(embed=utils.generate_embed(strings.HARVEST_STARTED, message.author.name, config.LINK_HARVEST))
                else:
                    await message.channel.send(embed=utils.generate_embed(strings.NOT_ELIGIBLE_FOR_PROCESS, message.author.name))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

        elif message.content == "!harvestInfo":
            try:
                current_process = db.get_current_process(message.author.id)
                if current_process == "harvest":
                    duration = db.get_duration(message.author.id, "harvest")
                    due_time = utils.get_time_after(db.get_checkpoint(message.author.id), duration)
                    if utils.is_elapsed(due_time):
                        await message.channel.send(embed=utils.generate_embed(strings.HARVEST_READY, message.author.name, config.LINK_HARVEST))
                    else:
                        await message.channel.send(embed=utils.generate_embed(strings.HARVEST_TIME_LEFT.format(utils.get_time_left(due_time)), message.author.name, config.LINK_HARVEST))
                else:
                    await message.channel.send(embed=utils.generate_embed(strings.NOT_CURRENTLY_HARVESTING, message.author.name))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

        elif message.content == "!harvestEnd":
            try:
                current_process = db.get_current_process(message.author.id)
                if current_process == "harvest":
                    duration = db.get_duration(message.author.id, "harvest")
                    due_time = utils.get_time_after(db.get_checkpoint(message.author.id), duration)
                    if utils.is_elapsed(due_time):
                        grape_production = db.get_harvest_base_production() * db.get_bonus(message.author.id, "harvest")
                        db.update_current_process(message.author.id, "harvest-winemaking", utils.get_checkpoint())
                        db.update_production(message.author.id, grape_production)
                        await message.channel.send(embed=utils.generate_embed(strings.HARVEST_DONE.format(utils.convert_to_thousands(grape_production)), message.author.name, config.LINK_HARVEST))
                    else:
                        await message.channel.send(embed=utils.generate_embed(strings.HARVEST_TIME_LEFT.format(utils.get_time_left(due_time)), message.author.name, config.LINK_HARVEST))
                else:
                    await message.channel.send(embed=utils.generate_embed(strings.NOT_CURRENTLY_HARVESTING, message.author.name))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

        elif message.content == "!winemaking":
            try:
                current_process = db.get_current_process(message.author.id)
                if current_process == "winemaking":
                    await message.channel.send(embed=utils.generate_embed(strings.WINEMAKING_IN_PROGRESS, message.author.name, config.LINK_WINEMAKING))
                elif current_process == "harvest-winemaking":
                    db.update_current_process(message.author.id, "winemaking", utils.get_checkpoint())
                    await message.channel.send(embed=utils.generate_embed(strings.WINEMAKING_STARTED, message.author.name, config.LINK_WINEMAKING))
                else:
                    await message.channel.send(embed=utils.generate_embed(strings.NOT_ELIGIBLE_FOR_PROCESS, message.author.name))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

        elif message.content == "!winemakingInfo":
            try:
                current_process = db.get_current_process(message.author.id)
                if current_process == "winemaking":
                    duration = db.get_duration(message.author.id, "winemaking")
                    due_time = utils.get_time_after(db.get_checkpoint(message.author.id), duration)
                    if utils.is_elapsed(due_time):
                        await message.channel.send(embed=utils.generate_embed(strings.WINEMAKING_READY, message.author.name, config.LINK_WINEMAKING))
                    else:
                        await message.channel.send(embed=utils.generate_embed(strings.WINEMAKING_TIME_LEFT.format(utils.get_time_left(due_time)), message.author.name, config.LINK_WINEMAKING))
                else:
                    await message.channel.send(embed=utils.generate_embed(strings.NOT_CURRENTLY_WINEMAKING, message.author.name))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

        elif message.content == "!bottling":
            try:
                current_process = db.get_current_process(message.author.id)
                if current_process == "winemaking":
                    duration = db.get_duration(message.author.id, "winemaking")
                    due_time = utils.get_time_after(db.get_checkpoint(message.author.id), duration)
                    if utils.is_elapsed(due_time):
                        bottles = db.get_production(message.author.id) * 0.75 * db.get_bonus(message.author.id, "winemaking")
                        db.update_current_process(message.author.id, "winemaking-selling", utils.get_checkpoint())
                        db.update_production(message.author.id, bottles)
                        await message.channel.send(embed=utils.generate_embed(strings.WINEMAKING_DONE.format(utils.convert_to_thousands(bottles)), message.author.name, config.LINK_WINEMAKING))
                    else:
                        await message.channel.send(embed=utils.generate_embed(strings.WINEMAKING_TIME_LEFT.format(utils.get_time_left(due_time)), message.author.name, config.LINK_WINEMAKING))
                else:
                    await message.channel.send(embed=utils.generate_embed(strings.NOT_CURRENTLY_WINEMAKING, message.author.name))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

        elif message.content == "!selling":
            try:
                current_process = db.get_current_process(message.author.id)
                if current_process == "selling":
                    await message.channel.send(embed=utils.generate_embed(strings.SELLING_IN_PROGRESS, message.author.name, config.LINK_SELLING))
                elif current_process == "winemaking-selling":
                    db.update_current_process(message.author.id, "selling", utils.get_checkpoint())
                    await message.channel.send(embed=utils.generate_embed(strings.SELLING_STARTED, message.author.name, config.LINK_SELLING))
                else:
                    await message.channel.send(embed=utils.generate_embed(strings.NOT_ELIGIBLE_FOR_PROCESS, message.author.name))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

        elif message.content == "!sellingInfo":
            try:
                current_process = db.get_current_process(message.author.id)
                if current_process == "selling":
                    duration = db.get_duration(message.author.id, "selling")
                    due_time = utils.get_time_after(db.get_checkpoint(message.author.id), duration)
                    money = int(db.get_production(message.author.id) * db.get_selling_base_price() * db.get_bonus(message.author.id, "selling") * utils.get_percentage_time_completed(db.get_checkpoint(message.author.id), duration))
                    await message.channel.send(embed=utils.generate_embed(strings.SELLING_TIME_LEFT.format(utils.get_time_left(due_time), utils.convert_to_thousands(money)), message.author.name, config.LINK_SELLING))
                else:
                    await message.channel.send(embed=utils.generate_embed(strings.NOT_CURRENTLY_SELLING, message.author.name))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

        elif message.content.startswith("!deleteWinery "):
            try:
                current_process = db.get_current_process(message.author.id)
                try:
                    winery_name = message.content.replace("!deleteWinery ", "")
                    if winery_name == db.get_winery_name(message.author.id):
                        db.delete_player_details(message.author.id)
                        await message.channel.send(embed=utils.generate_embed(strings.PLAYER_DELETED, message.author.name))
                    else:
                        await message.channel.send(embed=utils.generate_embed(strings.WINERY_NAME_MISMATCH.format(winery_name), message.author.name))
                except:
                    await message.channel.send(embed=utils.generate_embed(strings.INVALID_COMMAND, message.author.name))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

        elif message.content.startswith("!changeGrapeVariety "):
            try:
                current_process = db.get_current_process(message.author.id)
                try:
                    grape_variety = message.content.replace("!changeGrapeVariety ", "")
                    if grape_variety in ["Barbera", "Chardonnay", "Nebbiolo", "Arneis", "Dolcetto", "Cortese"]:
                        db.update_grape_variety(message.author.id, grape_variety)
                        await message.channel.send(embed=utils.generate_embed(strings.GRAPE_VARIETY_UPDATED.format(grape_variety), message.author.name))
                    else:
                        await message.channel.send(embed=utils.generate_embed(strings.WRONG_GRAPE_SELECTION, message.author.name))
                except:
                    await message.channel.send(embed=utils.generate_embed(strings.INVALID_COMMAND, message.author.name))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

        elif message.content.startswith("!newName "):
            try:
                current_process = db.get_current_process(message.author.id)
                try:
                    winery_name = message.content.replace("!newName ", "")
                    db.update_winery_name(message.author.id, winery_name)
                    await message.channel.send(embed=utils.generate_embed(strings.WINERY_NAME_UPDATED.format(winery_name), message.author.name))
                except:
                    await message.channel.send(embed=utils.generate_embed(strings.INVALID_COMMAND, message.author.name))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

        elif message.content == "!stats":
            try:
                current_process = db.get_current_process(message.author.id)
                if current_process == "harvest":
                    status = "harvesting"
                elif current_process == "harvest-winemaking":
                    status = "awaiting winemaking"
                elif current_process == "winemaking":
                    status = "winemaking"
                elif current_process == "winemaking-selling":
                    status = "awaiting selling"
                elif current_process == "selling":
                    status = "selling"
                else:
                    status = "awaiting harvest"
                await message.channel.send(embed=utils.generate_embed(strings.STATS.format(db.get_level(message.author.id, "harvest").split("_")[1],
                                                                                           db.get_level(message.author.id, "winemaking").split("_")[1],
                                                                                           db.get_level(message.author.id, "selling").split("_")[1], status,
                                                                                           utils.convert_to_thousands(db.get_balance(message.author.id))),
                                                                      message.author.name, config.LINK_STATS))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

        elif message.content == "!nextOperation":
            try:
                current_process = db.get_current_process(message.author.id)
                if current_process == "harvest":
                    next_operation = "!harvestEnd"
                elif current_process == "harvest-winemaking":
                    next_operation = "!winemaking"
                elif current_process == "winemaking":
                    next_operation = "!bottling"
                elif current_process == "winemaking-selling":
                    next_operation = "!selling "
                elif current_process == "selling":
                    next_operation = "!harvest"
                else:
                    next_operation = "!harvest"
                await message.channel.send(embed=utils.generate_embed(strings.NEXT_COMMAND.format(next_operation), message.author.name))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

        elif message.content == "!levelupVineyards":
            try:
                current_process = db.get_current_process(message.author.id)
                if current_process == "harvest":
                    await message.channel.send(embed=utils.generate_embed(strings.NO_LEVEL_HARVEST, message.author.name, config.LINK_LEVEL_UP))
                else:
                    level = db.get_level(message.author.id, "harvest")
                    level_up = int(level.split("_")[1]) + 1
                    next_level = f"HARVEST_{level_up}"
                    if next_level == "HARVEST_6":
                        await message.channel.send(embed=utils.generate_embed(strings.MAX_LEVEL_REACHED, message.author.name, config.LINK_LEVEL_UP))
                    else:
                        level_up_cost = db.get_level_cost(level)
                        if level_up_cost > db.get_balance(message.author.id):
                            await message.channel.send(embed=utils.generate_embed(strings.CANT_AFFORD_LEVEL_UP, message.author.name, config.LINK_LEVEL_UP))
                        else:
                            db.update_harvest_level(message.author.id, next_level)
                            db.update_balance_left(message.author.id, db.get_balance(message.author.id) - level_up_cost)
                            await message.channel.send(embed=utils.generate_embed(strings.HARVEST_LEVEL_UP.format(level_up), message.author.name, config.LINK_LEVEL_UP))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

        elif message.content == "!levelupWinery":
            try:
                current_process = db.get_current_process(message.author.id)
                if current_process == "winemaking":
                    await message.channel.send(embed=utils.generate_embed(strings.NO_LEVEL_WINEMAKING, message.author.name, config.LINK_LEVEL_UP))
                else:
                    level = db.get_level(message.author.id, "winemaking")
                    level_up = int(level.split("_")[1]) + 1
                    next_level = f"WINEMAKING_{level_up}"
                    if next_level == "WINEMAKING_6":
                        await message.channel.send(embed=utils.generate_embed(strings.MAX_LEVEL_REACHED, message.author.name, config.LINK_LEVEL_UP))
                    else:
                        level_up_cost = db.get_level_cost(level)
                        if level_up_cost > db.get_balance(message.author.id):
                            await message.channel.send(embed=utils.generate_embed(strings.CANT_AFFORD_LEVEL_UP, message.author.name, config.LINK_LEVEL_UP))
                        else:
                            db.update_winemaking_level(message.author.id, next_level)
                            db.update_balance_left(message.author.id, db.get_balance(message.author.id) - level_up_cost)
                            await message.channel.send(embed=utils.generate_embed(strings.WINEMAKING_LEVEL_UP.format(level_up), message.author.name, config.LINK_LEVEL_UP))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

        elif message.content == "!levelupMarketing":
            try:
                current_process = db.get_current_process(message.author.id)
                if current_process == "selling":
                    await message.channel.send(embed=utils.generate_embed(strings.NO_LEVEL_SELLING, message.author.name, config.LINK_LEVEL_UP))
                else:
                    level = db.get_level(message.author.id, "selling")
                    level_up = int(level.split("_")[1]) + 1
                    next_level = f"SELLING_{level_up}"
                    if next_level == "SELLING_6":
                        await message.channel.send(embed=utils.generate_embed(strings.MAX_LEVEL_REACHED, message.author.name, config.LINK_LEVEL_UP))
                    else:
                        level_up_cost = db.get_level_cost(level)
                        if level_up_cost > db.get_balance(message.author.id):
                            await message.channel.send(embed=utils.generate_embed(strings.CANT_AFFORD_LEVEL_UP, message.author.name, config.LINK_LEVEL_UP))
                        else:
                            db.update_selling_level(message.author.id, next_level)
                            db.update_balance_left(message.author.id, db.get_balance(message.author.id) - level_up_cost)
                            await message.channel.send(embed=utils.generate_embed(strings.SELLING_LEVEL_UP.format(level_up), message.author.name, config.LINK_LEVEL_UP))
            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

        elif message.content == "!help":
            await message.channel.send(embed=utils.generate_embed(strings.COMMANDS, message.author.name))

        elif message.content == "!leaderboard":
            leaderboard = db.get_leaderboard()
            leaderboard = [["Winery Name", "Grape Variety", "Balance"]] + leaderboard
            data = tabulate(leaderboard, headers="firstrow", floatfmt=".2f")
            duration = db.get_reset_duration()
            due_time = utils.get_time_after(db.get_reset_checkpoint(), duration)
            await message.channel.send(embed=utils.generate_embed(f"```{str(data)}```",
                                                                  message.author.name, config.LINK_LEADERBOARD,
                                                                  strings.LEADERBOARD_RESET.format(utils.get_days_left(due_time))))

        elif message.content == "!nextLevelInfo":
            try:
                current_process = db.get_current_process(message.author.id)

                harvest_level = db.get_level(message.author.id, "harvest")
                harvest_level_up = int(harvest_level.split("_")[1]) + 1
                harvest_next_level = f"HARVEST_{harvest_level_up}"
                if harvest_next_level == "HARVEST_6":
                    harvest_next_level == strings.MAX_LEVEL
                    old_grape_production = "--"
                    new_grape_production = "--"
                    perc_grape_increase = "--"
                    harvest_old_time = "--"
                    harvest_new_time = "--"
                    harvest_level_up_cost = "--"
                else:
                    harvest_level_up_cost = db.get_level_cost(harvest_level)
                    old_grape_production = int(db.get_harvest_base_production() * db.get_bonus(message.author.id, "harvest"))
                    new_grape_production = int(db.get_harvest_base_production() * db.get_bonus_from_cost_table(harvest_next_level))
                    perc_grape_increase = int((new_grape_production - old_grape_production) / old_grape_production * 100)
                    harvest_old_time = utils.convert_min_to_time(db.get_duration(message.author.id, "harvest"))
                    harvest_new_time = utils.convert_min_to_time(db.get_duration_from_cost_table(harvest_next_level))

                winemaking_level = db.get_level(message.author.id, "winemaking")
                winemaking_level_up = int(winemaking_level.split("_")[1]) + 1
                winemaking_next_level = f"WINEMAKING_{winemaking_level_up}"
                if winemaking_next_level == "WINEMAKING_6":
                    winemaking_next_level == strings.MAX_LEVEL
                    old_bottles = "--"
                    new_bottles = "--"
                    perc_bottles_increase = "--"
                    winemaking_old_time = "--"
                    winemaking_new_time = "--"
                    winemaking_level_up_cost = "--"
                else:
                    winemaking_level_up_cost = db.get_level_cost(winemaking_level)
                    ogp = db.get_harvest_base_production() * db.get_bonus(message.author.id, "harvest")
                    old_bottles = int(ogp * 0.75 * db.get_bonus(message.author.id, "winemaking"))
                    new_bottles = int(ogp * 0.75 * db.get_bonus_from_cost_table(winemaking_next_level))
                    perc_bottles_increase = int((new_bottles - old_bottles) / old_bottles * 100)
                    winemaking_old_time = utils.convert_min_to_time(db.get_duration(message.author.id, "winemaking"))
                    winemaking_new_time = utils.convert_min_to_time(db.get_duration_from_cost_table(winemaking_next_level))

                selling_level = db.get_level(message.author.id, "selling")
                selling_level_up = int(selling_level.split("_")[1]) + 1
                selling_next_level = f"SELLING_{selling_level_up}"
                if selling_next_level == "SELLING_6":
                    selling_next_level == strings.MAX_LEVEL
                    old_money = "--"
                    new_bottles = "--"
                    perc_money_increase = "--"
                    selling_old_time = "--"
                    selling_new_time = "--"
                    selling_level_up_cost = "--"
                else:
                    selling_level_up_cost = db.get_level_cost(selling_level)
                    ogp = db.get_harvest_base_production() * db.get_bonus(message.author.id, "harvest")
                    bottles = ogp * 0.75 * db.get_bonus(message.author.id, "winemaking")
                    old_money = int(bottles * db.get_selling_base_price() * db.get_bonus(message.author.id, "selling"))
                    new_money = int(bottles * db.get_selling_base_price() * db.get_bonus_from_cost_table(selling_next_level))
                    perc_money_increase = int((new_money - old_money) / old_money * 100)
                    selling_old_time = utils.convert_min_to_time(db.get_duration(message.author.id, "selling"))
                    selling_new_time = utils.convert_min_to_time(db.get_duration_from_cost_table(selling_next_level))

                await message.channel.send(embed=utils.generate_embed(strings.NEXT_LEVEL_INFO.format(utils.convert_to_thousands(harvest_level_up_cost), utils.convert_to_thousands(old_grape_production), utils.convert_to_thousands(new_grape_production), perc_grape_increase, harvest_old_time, harvest_new_time,
                                                                                                     utils.convert_to_thousands(winemaking_level_up_cost), utils.convert_to_thousands(old_bottles), utils.convert_to_thousands(new_bottles), perc_bottles_increase, winemaking_old_time, winemaking_new_time,
                                                                                                     utils.convert_to_thousands(selling_level_up_cost), utils.convert_to_thousands(old_money), utils.convert_to_thousands(new_money), perc_money_increase, selling_old_time, selling_new_time), message.author.name))

            except:
                await message.channel.send(embed=utils.generate_embed(strings.NO_WINERY, message.author.name))

#TODO add leaderboard and reset of leaderboard every week


async def user_metrics_background_task():
    await client.wait_until_ready()
    while True:
        guild = discord.utils.get(client.guilds, id=config.GUILD_ID)

        for row in db.get_all_selling():
            discord_id = row[0]
            duration = db.get_duration(discord_id, "selling")
            due_time = utils.get_time_after(row[4], duration)
            if utils.is_elapsed(due_time):
                money = db.get_production(discord_id) * db.get_selling_base_price() * db.get_bonus(discord_id, "selling")
                db.update_current_process(discord_id, "", utils.get_checkpoint())
                db.update_balance(discord_id, money)

                member = await guild.fetch_member(int(discord_id))
                await member.send(embed=utils.generate_embed(strings.SELLING_DONE.format(utils.convert_to_thousands(money),
                                                                                         utils.convert_to_thousands(db.get_balance(discord_id))), member.name, config.LINK_SELLING))


        duration = db.get_reset_duration()
        due_time = utils.get_time_after(db.get_reset_checkpoint(), duration)
        if utils.is_elapsed(due_time):
            db.reset_player_details()
            db.set_reset_checkpoint(utils.get_checkpoint())

        for i in range(1):
            await asyncio.sleep(1)

client.loop.create_task(user_metrics_background_task())
client.run(config.DISCORD_TOKEN)





























