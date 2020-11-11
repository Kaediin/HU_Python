import psycopg2
from psycopg2 import sql

connection = None
cursor = None


def open_db_connection():
    global connection, cursor
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Schouten2002",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")
        cursor = connection.cursor()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


def tweet_message(msg, name):
    from datetime import datetime
    currentdateTime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    query = sql.SQL('insert into ns_berichten.tweet values (default, %s, %s, %s, null, null)')
    data = (msg, name, currentdateTime)
    execute_query(query, data)
    # cursor.execute('insert into ns_berichten.tweet values (default, %s, %s, %s, null, null)',
    #                (msg, name, currentdateTime))
    print('Message saved to db')



def add_moderator(first_name, infix, last_name):
    cursor.execute('insert into ns_berichten.moderator values (default, %s, %s, %s)',
                   (first_name, infix, last_name))



def add_scherm(name, location):
    cursor.execute('insert into ns_berichten.scherm values (default, %s, %s)',
                   (location, name))

def close_db_connection():
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


def execute_query(query, data):
    open_db_connection()

    cursor.execute(query, data)
    connection.commit()

    close_db_connection()
