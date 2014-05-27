import psycopg2
import sys

def main():

    #get a connection, if a connection cannot be made, an exception is thrown
    global conn
    conn = psycopg2.connect(database="chatapp_db", user="postgres", password="db2013.", host="localhost");
    
    #conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print "Connected!\n"
    
    

def insert(message):
    cursor = conn.cursor();
    cursor.execute("INSERT INTO messages(message_text) VALUES('%d')" % message)
    
    conn.commit()
    print "Records created successfully";
    conn.close()
    

if __name__ == "__main__":
    main()