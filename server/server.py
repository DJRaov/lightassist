# LightAssist Server v0.1
# Main thread

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