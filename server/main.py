#    __---LightAssist Server---___
#                v0.1

#import standard libs
import os, math, signal, time, platform

#import modules
import server

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

#ctrl-c handler
def sigint_handler(signum, frame):
    res = input("Do you want to shut down LightAssist Server? (y/N)")
    if res == 'y' or "Y":
        server_shutdown()
    if res == "n" or "N":
        return

#henlo
print("LightAssist v",ver,"Server\n----------")

#begin init
server.init_server()

print("\n\n",end="")
while True:
    cmd = input(">",end="")
    if cmd:
        la_server.cmdhandler(cmd)
