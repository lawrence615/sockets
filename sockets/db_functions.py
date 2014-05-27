import database

def newmessage(message):
    database.insert(message)
    