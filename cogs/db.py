import sqlite3

import cogs.config as config
import cogs.utils as utils

conn = sqlite3.connect(config.DATABASE_NAME)

def initializeDB():
    conn.execute('''CREATE TABLE IF NOT EXISTS PLAYER_DETAILS
                 (DISCORD_ID TEXT PRIMARY KEY NOT NULL,
                 WINERY_NAME TEXT,
                 GRAPE_VARIETY TEXT,
                 CURRENT_PROCESS TEXT,
                 CHECKPOINT TEXT,
                 HARVEST_LEVEL TEXT,
                 WINEMAKING_LEVEL TEXT,
                 SELLING_LEVEL TEXT,
                 PRODUCTION TEXT,
                 BALANCE TEXT,
                 TRACKER TEXT);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS COST_TABLE
                 (ID TEXT PRIMARY KEY NOT NULL,
                 LEVEL_UP_COST TEXT,
                 BONUS TEXT,
                 DURATION TEXT);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS VARIABLES
                 (NAME TEXT PRIMARY KEY NOT NULL,
                 VALUE TEXT);''')


    try:
        insert_variable("reset_checkpoint", "2022-02-14 00:00:00.0")
        insert_variable("reset_duration", "20160")
        insert_cost_table("HARVEST_1", "7000", "1", "720")
        insert_cost_table("HARVEST_2", "14000", "2", "600")
        insert_cost_table("HARVEST_3", "150000", "3", "480")
        insert_cost_table("HARVEST_4", "1000000", "4", "360")
        insert_cost_table("HARVEST_5", "-", "5", "240")
        insert_cost_table("WINEMAKING_1", "7000", "0.5", "360")
        insert_cost_table("WINEMAKING_2", "14000", "0.55", "300")
        insert_cost_table("WINEMAKING_3", "150000", "0.6", "240")
        insert_cost_table("WINEMAKING_4", "1000000", "0.7", "180")
        insert_cost_table("WINEMAKING_5", "-", "0.75", "120")
        insert_cost_table("SELLING_1", "7000", "1", "240")
        insert_cost_table("SELLING_2", "14000", "2", "210")
        insert_cost_table("SELLING_3", "150000", "3", "180")
        insert_cost_table("SELLING_4", "1000000", "4", "150")
        insert_cost_table("SELLING_5", "-", "5", "120")
        insert_variable("harvest_base_production", "9000")
        insert_variable("selling_base_price", "7")
    except:
        pass

    conn.commit()

def insert_player_details(discord_id):
    sqlite_insert_with_param = """INSERT INTO 'PLAYER_DETAILS'
    ('DISCORD_ID', 'WINERY_NAME', 'GRAPE_VARIETY', 'CURRENT_PROCESS', 'CHECKPOINT', 'HARVEST_LEVEL', 'WINEMAKING_LEVEL', 'SELLING_LEVEL', 'PRODUCTION', 'BALANCE', 'TRACKER')
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    data_tuple = (str(discord_id), "", "", "", "", "HARVEST_1", "WINEMAKING_1", "SELLING_1", "", "0", "winery_name")
    conn.execute(sqlite_insert_with_param, data_tuple)
    conn.commit()

def insert_cost_table(id, level_up, bonus, duration):
    sqlite_insert_with_param = """INSERT INTO 'COST_TABLE'
    ('ID', 'LEVEL_UP_COST', 'BONUS', 'DURATION')
    VALUES (?, ?, ?, ?);"""
    data_tuple = (id, level_up, bonus, duration)
    conn.execute(sqlite_insert_with_param, data_tuple)
    conn.commit()

def insert_variable(name, value):
    sqlite_insert_with_param = """INSERT INTO 'VARIABLES'
    ('NAME', 'VALUE')
    VALUES (?, ?);"""
    data_tuple = (name, value)
    conn.execute(sqlite_insert_with_param, data_tuple)
    conn.commit()

def update_current_process(discord_id, process, checkpoint):
    conn.execute(f"UPDATE PLAYER_DETAILS SET CURRENT_PROCESS='{process}', CHECKPOINT='{checkpoint}' WHERE DISCORD_ID='{str(discord_id)}'")
    conn.commit()

def get_level(discord_id, process):
    return conn.execute(f"SELECT {process.upper()}_LEVEL FROM PLAYER_DETAILS WHERE DISCORD_ID='{str(discord_id)}'").fetchone()[0]

def get_duration(discord_id, process):
    id = get_level(discord_id, process)
    return conn.execute(f"SELECT DURATION FROM COST_TABLE WHERE ID='{id}'").fetchone()[0]

def get_checkpoint(discord_id):
    return conn.execute(f"SELECT CHECKPOINT FROM PLAYER_DETAILS WHERE DISCORD_ID='{str(discord_id)}'").fetchone()[0]

def get_tracker(discord_id):
    try:
        return conn.execute(f"SELECT TRACKER FROM PLAYER_DETAILS WHERE DISCORD_ID='{str(discord_id)}'").fetchone()[0]
    except:
        return ""

def update_tracker(discord_id, tracker):
    conn.execute(f"UPDATE PLAYER_DETAILS SET TRACKER='{tracker}' WHERE DISCORD_ID='{str(discord_id)}'")
    conn.commit()

def update_winery_name(discord_id, winery_name):
    winery_name = winery_name.replace("'", "")
    conn.execute(f"UPDATE PLAYER_DETAILS SET WINERY_NAME='{winery_name}' WHERE DISCORD_ID='{str(discord_id)}'")
    conn.commit()

def update_grape_variety(discord_id, grape_variety):
    conn.execute(f"UPDATE PLAYER_DETAILS SET GRAPE_VARIETY='{grape_variety}' WHERE DISCORD_ID='{str(discord_id)}'")
    conn.commit()

def get_current_process(discord_id):
    return conn.execute(f"SELECT CURRENT_PROCESS FROM PLAYER_DETAILS WHERE DISCORD_ID='{str(discord_id)}'").fetchone()[0]

def get_harvest_base_production():
    return int(conn.execute(f"SELECT VALUE FROM VARIABLES WHERE NAME='harvest_base_production'").fetchone()[0])

def get_selling_base_price():
    return int(conn.execute(f"SELECT VALUE FROM VARIABLES WHERE NAME='selling_base_price'").fetchone()[0])

def get_bonus(discord_id, process):
    id = get_level(discord_id, process)
    return float(conn.execute(f"SELECT BONUS FROM COST_TABLE WHERE ID='{id}'").fetchone()[0])

def get_bonus_from_cost_table(id):
    return float(conn.execute(f"SELECT BONUS FROM COST_TABLE WHERE ID='{id}'").fetchone()[0])

def update_production(discord_id, production):
    conn.execute(f"UPDATE PLAYER_DETAILS SET PRODUCTION='{str(production)}' WHERE DISCORD_ID='{str(discord_id)}'")
    conn.commit()

def get_production(discord_id):
    return float(conn.execute(f"SELECT PRODUCTION FROM PLAYER_DETAILS WHERE DISCORD_ID='{str(discord_id)}'").fetchone()[0])

def get_all_selling():
    return conn.execute("SELECT * FROM PLAYER_DETAILS WHERE CURRENT_PROCESS='selling'")

def get_balance(discord_id):
    return float(conn.execute(f"SELECT BALANCE FROM PLAYER_DETAILS WHERE DISCORD_ID='{str(discord_id)}'").fetchone()[0])

def update_balance(discord_id, balance):
    conn.execute(f"UPDATE PLAYER_DETAILS SET BALANCE='{str(balance + get_balance(discord_id))}' WHERE DISCORD_ID='{str(discord_id)}'")
    conn.commit()

def get_winery_name(discord_id):
    return conn.execute(f"SELECT WINERY_NAME FROM PLAYER_DETAILS WHERE DISCORD_ID='{str(discord_id)}'").fetchone()[0]

def delete_player_details(discord_id):
    conn.execute(f"DELETE FROM PLAYER_DETAILS WHERE DISCORD_ID='{str(discord_id)}'")
    conn.commit()

def get_level_cost(id):
    return int(conn.execute(f"SELECT LEVEL_UP_COST FROM COST_TABLE WHERE ID='{id}'").fetchone()[0])

def update_harvest_level(discord_id, level):
    conn.execute(f"UPDATE PLAYER_DETAILS SET HARVEST_LEVEL='{str(level)}' WHERE DISCORD_ID='{str(discord_id)}'")
    conn.commit()

def update_winemaking_level(discord_id, level):
    conn.execute(f"UPDATE PLAYER_DETAILS SET WINEMAKING_LEVEL='{str(level)}' WHERE DISCORD_ID='{str(discord_id)}'")
    conn.commit()

def update_selling_level(discord_id, level):
    conn.execute(f"UPDATE PLAYER_DETAILS SET SELLING_LEVEL='{str(level)}' WHERE DISCORD_ID='{str(discord_id)}'")
    conn.commit()

def update_balance_left(discord_id, balance):
    conn.execute(f"UPDATE PLAYER_DETAILS SET BALANCE='{str(balance)}' WHERE DISCORD_ID='{str(discord_id)}'")
    conn.commit()

def get_duration_from_cost_table(id):
    return int(conn.execute(f"SELECT DURATION FROM COST_TABLE WHERE ID='{id}'").fetchone()[0])

def get_leaderboard():
    data = conn.execute(f"SELECT * FROM PLAYER_DETAILS ORDER BY CAST(BALANCE AS FLOAT) DESC LIMIT 10")
    return [[row[1], row[2], f"${utils.convert_to_thousands(int(float((row[9]))))}"] for row in data]

def get_reset_duration():
    return int(conn.execute(f"SELECT VALUE FROM VARIABLES WHERE NAME='reset_duration'").fetchone()[0])

def get_reset_checkpoint():
    return conn.execute(f"SELECT VALUE FROM VARIABLES WHERE NAME='reset_checkpoint'").fetchone()[0]

def reset_player_details():
    conn.execute(f"UPDATE PLAYER_DETAILS SET CURRENT_PROCESS='', CHECKPOINT='', HARVEST_LEVEL='HARVEST_1', WINEMAKING_LEVEL='WINEMAKING_1', SELLING_LEVEL='SELLING_1', PRODUCTION='', BALANCE='0', TRACKER=''")
    conn.commit()

def set_reset_checkpoint(checkpoint):
    conn.execute(f"UPDATE VARIABLES SET VALUE='{str(checkpoint)}' WHERE NAME='reset_checkpoint'")
    conn.commit()