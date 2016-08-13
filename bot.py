# python 3.5
#
# sudo apt-get install python-pip
# sudo pip install telepot
# sudo pip install watchdog
#

import os
import sys
import time
import telepot
import pickle
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

userdb = set();
password = "P@ssw0rd"
userdb_filename = "user.db"
monitor_path = "/tmp"
teletoken='***TELEGRAM BOT TOKEN***'

class ChangeHandler(FileSystemEventHandler):
    def on_created(self, event):
        print (event.src_path + ' ' + event.event_type)
        if event.is_directory:
            return
        if (os.path.splitext(event.src_path)[-1].lower()  == '.jpg'):
            for chats in userdb:
                f = open(event.src_path, 'rb')
                bot.sendPhoto(chats, f, caption = event.src_path)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        output = msg['text'].split()
        print (output, len(output))

        if (output[0] == '/start' and len(output)>1):
            if (output[1] == password):
                userdb.add(chat_id)
                print (userdb)
                dbf = open(userdb_filename, 'wb')
                pickle.dump(userdb, dbf)
                dbf.close()
                bot.sendMessage(chat_id, 'Start working!')
            else:
                bot.sendMessage(chat_id, 'Wrong password')
        elif (output[0] == '/start' and len(output)<=1):
            bot.sendMessage(chat_id, 'Syntax: /start [password]')
        elif output[0] == '/stop':
            userdb.discard(chat_id)
            dbf = open(userdb_filename, 'wb')
            pickle.dump(userdb, dbf)
            dbf.close()
            bot.sendMessage(chat_id, 'Stop working!')

try:
    dbf = open(userdb_filename,'rb')
    userdb = pickle.load(dbf)
    dbf.close()
except:
    userdb = set()

print (userdb)
bot = telepot.Bot(teletoken)
bot.message_loop(handle)

# Keep the program running.
while True:
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, monitor_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
