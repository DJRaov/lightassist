#    __---LightAssist Server---___
#                v0.1

import os, math, signal, time, platform

#python version check
pyver = platform.python_version()
versplit = pyver.split('.')
if int(versplit[0]) << 3 and int(versplit[1]) < 10:
    print("Incompatible Python version! LightAssist requires Python 3.10 and up, you have",pyver,".")
    exit(1)

#dependency check
try:
    import psycopg2
except:
    print("psycopg2 not found! Please install.")
    exit(1)

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

#henlo
print("LightAssist v",ver,"Server\n----------")

#begin init
try:
    database = psycopg2.connect(host="localhost", database="traffic",user="server",password="yourpasswordhere")
except Exception as issue:
    print("Failed to connect to LightAssist database!\nException encountered:",issue)
finally:
    print("Connected to database!")
db = database.cursor() 

print("\n\n>")
while True:
    cmd = input()
    match cmd:
        case "exit":
            server_shutdown()
        case "quit":
            server_shutdown()



