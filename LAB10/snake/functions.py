import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def create_tables():
    commands = (
        '''
        CREATE TABLE snake (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) UNIQUE NOT NULL,
            user_score INTEGER,
            user_lenght INTEGER,
            user_level INTEGER,
            user_fps INTEGER
        )
        ''',
        '''
        CREATE TABLE walls (
            user_name VARCHAR(255),
            x_cord INTEGER NOT NULL,
            y_cord INTEGER NOT NULL
        )
        ''',
        '''
        CREATE TABLE snakes(
            user_name VARCHAR(255),
            x_snake INTEGER,
            y_snake INTEGER
        )
        '''
    )
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def check_name(user_name):
    conn = None
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute('SELECT * FROM snake WHERE user_name = %s', (user_name,))
    result = cur.fetchone()
    if result is not None and len(result) > 0:
        cur.close()
        conn.close()
        return True
    else:
        cur.close()
        conn.close()
        return False
    
def add_new_user(user_name, user_score = 0, user_lenght = 1, user_level = 1, user_fps = 10):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('INSERT INTO snake(user_name, user_score, user_lenght, user_level, user_fps) VALUES(%s,%s,%s,%s,%s)',(user_name, user_score, user_lenght, user_level, user_fps))
        cur.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def save_data_user(user_name, user_score, user_lenght, user_level, user_fps):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('''UPDATE snake
                         SET user_score = %s,
                             user_lenght = %s,
                             user_level = %s,
                             user_fps = %s
                         WHERE user_name = %s''',(user_score, user_lenght, user_level, user_fps, user_name))
        cur.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def save_wall(user_name, x_cord, y_cord):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('INSERT INTO walls(user_name,x_cord,y_cord) VALUES(%s,%s,%s)', (user_name, x_cord, y_cord))
        cur.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def save_snake(user_name, x_snake, y_snake):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('INSERT INTO snakes(user_name,x_snake,y_snake) VALUES(%s,%s,%s)', (user_name, x_snake, y_snake))
        cur.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def get_data_user(user_name):
    conn = None
    mylist = []
    cords = []
    snakes = []
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT user_score, user_lenght, user_level, user_fps FROM snake WHERE user_name = %s', (user_name, ))
        rows = cur.fetchone()
        mylist = rows
        cur.execute('SELECT x_cord, y_cord FROM walls WHERE user_name = %s', (user_name, ))
        rows = cur.fetchall()
        for row in rows:
            cords.append(row)
        cur.execute('SELECT x_snake, y_snake FROM snakes WHERE user_name = %s', (user_name, ))
        rows = cur.fetchall()
        for row in rows:
            snakes.append(row)
        cur.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return mylist, cords, snakes

def delete_data(user_name):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('DELETE FROM snake WHERE user_name = %s', (user_name,))
        cur.execute('DELETE FROM walls WHERE user_name = %s', (user_name,))
        cur.execute('DELETE FROM snakes WHERE user_name = %s', (user_name,))
        cur.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        
def delete_all():
    sql = '''DELETE FROM snake'''
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        print('Удалено строк:', cur.rowcount)
        cur.execute('DELETE FROM walls')
        print('Удалено строк:', cur.rowcount)
        cur.execute('DELETE FROM snakes')
        print('Удалено строк:', cur.rowcount)
        cur.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()