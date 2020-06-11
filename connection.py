import psycopg2
from psycopg2 import extras
import os


def fetch_all(query, parameters):
    connection = get_connection()
    cur = connection.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute(query, parameters)
    result = cur.fetchall()
    cur.close()
    connection.close()
    return result


def execute_query(query, parameters):
    connection = get_connection()
    cur = connection.cursor()
    cur.execute(query, parameters)
    result = ''
    try:
        result = cur.fetchone()
    except psycopg2.ProgrammingError as pe:
        pass
    cur.close()
    connection.close()
    return result


def get_connection():
    try:
        connection_string = os.environ.get('connection_string')
        conn = psycopg2.connect(connection_string)
        return conn
    except:
        print("I am unable to connect to the database")
