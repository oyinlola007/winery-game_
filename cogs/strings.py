WELCOME_TO_WINERY = "Welcome to the winery!\n\nPlease reply with your winery name to continue"
WINERY_EXISTS = "User already has a functional winery!\n\nReply with _**!nextOperation**_ to view your next operation or _**!deletewinery**_ to delete your winery"
WINERY_NAME_ENTERED = """Your winery name has been set to **{}**. You can change your winery name later on with _**!newName**_

Please reply with your grape variety from the list below:
◉ Barbera
◉ Chardonnay
◉ Nebbiolo
◉ Arneis
◉ Dolcetto
◉ Cortese"""

WRONG_GRAPE_SELECTION = """The grape you entered does not exist!

Select your grape variety from the list below:
◉ Barbera
◉ Chardonnay
◉ Nebbiolo
◉ Arneis
◉ Dolcetto
◉ Cortese"""

GRAPE_VARIETY_ENTERED = "Your grape variety has been set to **{}**. You can change your grape variety later on with _**!changeGrapeVariety**_\n\nPlease reply with _**!help**_ to view the list of commands"
NO_WINERY = "You do not have a functional winery!\n\nReply with _**!newwinery**_ to create a new winery"
NOT_ELIGIBLE_FOR_PROCESS = "You are not eligible for the process!\n\nReply with _**!nextOperation**_ to view your next operation"

HARVEST_IN_PROGRESS = "You are already in harvesting process!\n\nReply with _**!harvestInfo**_ to view how much time is left before harvesting is done"
HARVEST_STARTED = "Harvesting has started!\n\nReply with _**!harvestInfo**_ to view how much time is left before harvesting is done"
HARVEST_READY = "Harvesting is done!\n\nReply with _**!harvestEnd**_ to collect your harvest"
HARVEST_TIME_LEFT = "Time left before harvesting is done: **{}**\n\nReply with _**!harvestEnd**_ to collect your harvest when the time is up"
NOT_CURRENTLY_HARVESTING = "You are not currently harvesting!\n\nReply with _**!nextOperation**_ to view your next operation"
HARVEST_DONE = "Harvest collected!\nYour base production was: **{}kg grapes**\n\nReply with _**!winemaking**_ to start wine production"

WINEMAKING_IN_PROGRESS = "You are already in winemaking process!\n\nReply with _**!winemakingInfo**_ to view how much time is left before winemaking is done"
WINEMAKING_STARTED = "Winemaking has started!\n\nReply with _**!winemakingInfo**_ to view how much time is left before winemaking is done"
WINEMAKING_READY = "Winemaking is done!\n\nReply with _**!bottling**_ to collect your wine bottles"
WINEMAKING_TIME_LEFT = "Time left before winemaking is done: **{}**\n\nReply with _**!bottling**_ to collect your wine bottles when the time is up"
NOT_CURRENTLY_WINEMAKING = "You are not currently winemaking!\n\nReply with _**!nextOperation**_ to view your next operation"
WINEMAKING_DONE = "Bottles collected!\nYour production was: **{} bottles**\n\nReply with _**!selling**_ to start selling"

SELLING_IN_PROGRESS = "You already started selling!\n\nReply with _**!sellingInfo**_ to view how much time is left before selling is done"
SELLING_STARTED = "Selling has started!\n\nReply with _**!sellingInfo**_ to view how much time is left before selling is done"
SELLING_TIME_LEFT = "Time left before selling is done: **{}**\n\nSo far, you have made **${}**"
NOT_CURRENTLY_SELLING = "You are not currently selling!\n\nReply with _**!nextOperation**_ to view your next operation"
SELLING_DONE = "Bottles sold!\n\nYou made a sum of: **${}**\nYour total balance is: **${}**\n\nReply with _**!harvest**_ to start harvesting again or _**!help**_ to see the list of commands on how to level up"

INVALID_COMMAND = "Invalid command!\n\nReply with _**!help**_ to view the list of commands"
PLAYER_DELETED = "Winery deleted!\n\nReply with _**!startwinery**_ to create a new winery"
WINERY_NAME_MISMATCH = "{} does not match the one you entered earlier!\n\nYou'll need to enter the exact winery name to delete the winery"
GRAPE_VARIETY_UPDATED = "Grape variety updated to **{}**"
WINERY_NAME_UPDATED = "Winery name updated to **{}**"
STATS = """Harvest Level : **{}**
Winemaking Level : **{}**
Selling Level : **{}**
Status : **{}**
Total Balance : **${}**"""
NEXT_COMMAND = "Use this command for your next operation: _**{}**_"

NO_LEVEL_HARVEST = "You can't perform this action while harvest is ongoing!\n\nReply with _**!levelupWinery**_ to upgrade winemaking level or _**!levelupMarketing**_ to upgrade marketing level"
NO_LEVEL_WINEMAKING = "You can't perform this action while winemaking is ongoing!\n\nReply with _**!levelupVineyards**_ to upgrade harvesting level or _**!levelupMarketing**_ to upgrade marketing level"
NO_LEVEL_SELLING = "You can't perform this action while selling is ongoing!\n\nReply with _**!levelupVineyards**_ to upgrade harvesting level or _**!levelupWinemaking**_ to upgrade winemaking level"

MAX_LEVEL_REACHED = "You have reached the maximum level for this process!\n\nReply with _**!stats**_ to view your current stats"
CANT_AFFORD_LEVEL_UP = "You can't afford to level up this process!\n\nReply with _**!nextLevelInfo**_ to view the cost of your next level up"

HARVEST_LEVEL_UP = "Your harvesting level has been increased to **Level {}**!\n\nReply with _**!nextLevelInfo**_ to view the cost of your next level up"
WINEMAKING_LEVEL_UP = "Your winemaking level has been increased to **Level {}**!\n\nReply with _**!nextLevelInfo**_ to view the cost of your next level up"
SELLING_LEVEL_UP = "Your selling level has been increased to **Level {}**!\n\nReply with _**!nextLevelInfo**_ to view the cost of your next level up"

COMMANDS = """_**!help**_ : Opens the command summary and help panel

_**!startWinery**_ : Create a new Winery

_**!deleteWinery [winery name]**_ : Delete a Winery (is case sensitive)

_**!changeGrapeVariety [new grape variety]**_ : Change the grape variety

_**!newName**_ : change winery name

_**!stats**_ : show the 3 field of action level, status and overall money

_**!leaderboard**_ : shows top 10 players

_**!levelupWinery**_ : level up Winery (Can't be used if Bottling is ongoing)

_**!levelupVineyards**_ : level up Vineyards (Can't be used if Harvest is ongoing)

_**!levelupMarketing**_ : level up Marketing (Can't be used if Selling is ongoing)

_**!nextLevelInfo**_ : show info of the next level of Winery, vineyards, marketing such as:
                - cost to level up
                - production increase
                - Activity Time

_**!nextOperation**_ : shows next operation required of user

_**!harvest**_ : Start the grape harvesting

_**!harvestInfo**_ : Shows how much time is left before harvesting is done

_**!harvestEnd**_ : Collect the Harvest result

_**!winemaking**_ : Start wine production

_**!winemakingInfo**_ : Show how much time is left before the winemaking is done

_**!bottling**_ : Collect the wine bottles

_**!selling**_ : Start selling

_**!sellingInfo**_ : Show how much time is left before the selling is done"""

MAX_LEVEL = "MAX LEVEL REACHED"

NEXT_LEVEL_INFO = """**Harvesting**
Cost : **${}**
Production increase from {}kg to {}kg -- **{}%**
Activity time reduction from {} to {}

**Winemaking**
Cost : **${}**
Bottles increase from {} to {} -- **{}%**
Activity time reduction from {} to {}

**Selling**
Cost : **${}**
Sales increase from ${} to ${} -- **{}%**
Activity time reduction from {} to {}
"""

LEADERBOARD_RESET = "Leaderboard will reset in: {}"