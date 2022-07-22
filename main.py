# bot.py
from fileinput import close
import os
# VIEW DB at C:\Users\Jason Jiang\custom-order-handling-bot\master.db
# Importanting sensitiveInfo/importantusers.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, './sensitiveInfo')

import importantusers
import json
#TODO: 
# create visual for order
# create system for people to take on orders
    # causes them to be invited in a thread
    # pin a order message
# create systems to drop orders
    #causes them to be droped from the thread
# create commands to see your active order
    #links to your special threads
# catch finished submission
#command to see all unverified/not sent to customer submissions
# sample users testing
# create email hooks

import sqlite3
import discord
def runServer(TOKEN):
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
    
    @client.event
    async def on_message(message):
        #dont respond to my own messages
        if message.author == client.user:
            return
        if (message.channel.id == importantusers.ORDERSALERTCHANNEL):
            if message.author.id == importantusers.JASONID:
                await message.channel.send('Jason identified')
                print(message.content)
                order = json.loads(message.content)
                print(order)
                cursor.execute(f"INSERT INTO ComikInkOrders VALUES ('{ order['name-1'] }', '{order['email-1']}', '{order['textarea-1']}', '{order['upload-1']}')")
                connection.commit()

            if message.author.id == importantusers.ALERTBOTID:
                await message.channel.send('ALERTBOT identified')
            
    client.run(TOKEN)

# TODO: insure that docker doesnt have permission issues wth db
connection = sqlite3.connect("master.db")
cursor = connection.cursor()
# NOTE Order is a key work // cannot name table order

cursor.execute('''CREATE TABLE IF NOT EXISTS ComikInkOrders (
    name TEXT,
    email TEXT,
    image_url TEXT,
    description TEXT
    )'''
)
cursor = connection.cursor()

with open("sensitiveInfo/discordtoken.txt") as discordtokenfile:
    TOKEN = discordtokenfile.read()
runServer(TOKEN)
