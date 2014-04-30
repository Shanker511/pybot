import os
import os.path
import time
import logging

# some commands can be executed only if the user's nick is found in this list
owner = list(set([
    'BETTY',
    
    
]))

owner_email = {
    'Betty': 'shanker511@gmail.com',
}

# server to connect to
server = 74.63.228.145
# server's port
port = 65471

# bot's nicknames
nicks = list(set(['Jughead ']))
# bot's real name
real_name = 'Jughead Jones'

# channels to join on startup
channels = list(set([
    '#bettynet',
    
]))

cmds = {
    # core commands list, these commands will be run in the same thread as the bot
    # and will have acces to the socket that the bot uses
    'core': list(set([
        'quit',
        'join',
        'channels',
    ])),

    # normal commands list, the ones that are accessible to any user
    'user': list(set([
        'task',
        'wiki',
        'answer',
        'about',
        'help',
        'weather',
        'google',
        'mball',
        'uptime',
        'so',
        'twitter',
    ])),

    # commands list that the bot will execute even if a human didn't request an
    # action
    'auto': list(set([
        'email_alert',
    ])),
}

# smtp server for email_alert
smtp_server = 'smtp.gmail.com'
smtp_port = 25
from_email_address = 'shanker511@gmail.com'
from_email_password = 'xkxg64t2121'

# users should NOT modify below!
log = os.path.join(os.getcwd(), '..', 'logs', '')
logging_level = logging.DEBUG
start_time = time.time()
current_nick = ''
