#    __---LightAssist Server---___
#                v0.1

import os, math, signal, time, platform

#python version check
pyver = platform.python_version()
versplit = pyver.split('.')
if int(versplit[0]) << 3 and int(versplit[1]) < 10:
    print("Incompatible Python version! LightAssist requires Python 3.10 and up, you have",pyver,". Exiting.")
    exit(1)

#dependency check
try:
    import psycopg2
except:
    print("psycopg2 not found! Installing it for you.")
    os.system("pip install psycopg2 --quiet")

ver = float(0.1)

def sigint_handler(signum, frame):
    res = input("Do you want to shut down LightAssist Server? (y/N)")
    if res == 'y':
        server_shutdown()

def server_shutdown():
    if database != None:
        try:
            print("LightAssist Server shutting down!")
            database.close()
        except Exception as issue:
            print("Could not gracefully close database connection! Exception encountered:",issue)
            exit(1)
        exit()

def init_server():
    try:
        database = psycopg2.connect(host="localhost", database="traffic",user="server",password="yourpasswordhere")
    except Exception as issue:
        print("Failed to connect to LightAssist database!\nException encountered:",issue)
        exit()
    if database != None:
        print("Connected to database!")
        db = database.cursor() 

def cmdhandler(cmd):
    match cmd:
        case "version":
            print("LightAssist v",ver)
            return
        case "exit" or "quit":
            server_shutdown()
        case "":
            return

#henlo
print("LightAssist v",ver,"Server\n----------")

#begin init
init_server()

print("\n\n",end="")
while True:
    cmd = input(">",end="")
    if cmd:
        cmdhandler(cmd)
