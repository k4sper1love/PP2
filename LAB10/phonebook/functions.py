import psycopg2, csv
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
        CREATE TABLE phonebook (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL,
            user_phone VARCHAR(12) UNIQUE NOT NULL 
        )
        ''',
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

def add_data_from_console(user_name, user_phone):
    sql = '''INSERT INTO phonebook(user_name, user_phone)
             VALUES(%s,%s) RETURNING user_id'''
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_name, user_phone))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return user_id

def add_data_from_csv(name_csv):
    sql = '''INSERT INTO phonebook(user_name, user_phone) VALUES(%s,%s)'''
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        with open('LAB10/phonebook/{0}.csv'.format(name_csv), 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(row)
                cur.execute(sql, (row[0], row[1]))
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def update_name(user_id, new_name, method, method2):
    if method == 1 and method2 == 1:
        sql = """UPDATE phonebook
                    SET user_name = %s
                    WHERE user_id = %s"""
    elif method == 2 and method2 == 1:
        sql = """UPDATE phonebook
                    SET user_name = %s
                    WHERE user_phone = %s"""
    elif method == 1 and method2 == 2:
        sql = """UPDATE phonebook
                    SET user_phone = %s
                    WHERE user_id = %s"""
    elif method == 2 and method2 == 2:
        sql = """UPDATE phonebook
                    SET user_phone = %s
                    WHERE user_phone = %s"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (new_name, str(user_id)))
        cur.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def get_data(user_id, method, method2, order = 'user_id'):
    if method == 1 and method2 == 1:
        sql = '''SELECT user_id, user_name, user_phone FROM phonebook WHERE user_id = %s ORDER BY user_id'''
    elif method == 1 and method2 == 2:
        sql = '''SELECT user_id, user_name, user_phone FROM phonebook WHERE user_phone = %s ORDER BY user_id'''
    elif method == 1 and method2 == 3:
        sql = '''SELECT user_id, user_name, user_phone FROM phonebook WHERE user_name = %s ORDER BY user_id'''
    elif method == 2 and order == 'user_id':
        sql = '''SELECT user_id, user_name, user_phone FROM phonebook ORDER BY user_id'''
    elif method == 2 and order == 'user_name':
        sql = '''SELECT user_id, user_name, user_phone FROM phonebook ORDER BY user_name'''
    elif method == 2 and order == 'user_phone':
        sql = '''SELECT user_id, user_name, user_phone FROM phonebook ORDER BY user_phone''' 
    elif method == 3 and method2 == 1:
        sql = '''SELECT user_id FROM phonebook'''
    elif method == 3 and method2 == 2:
        sql = '''SELECT user_name FROM phonebook'''
    elif method == 3 and method2 == 3:
        sql = '''SELECT user_phone FROM phonebook'''
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_id,))
        print('Найдено строк:', cur.rowcount)
        rows = cur.fetchall()
        number = 1
        for row in rows:
            if method == 3 and method2 == 1:
                print('{0} - id: {1}'.format(number,row[0]))
            elif method == 3 and method2 == 2:
                print('{0} - Имя: {1}'.format(number,row[0]))
            elif method == 3 and method2 == 3:
                print('{0} - Номер телефона:: {1}'.format(number,row[0]))
            else:
                print('{0} - id: {1}, Имя: {2}, Номер телефона: {3}'.format(number,row[0], row[1], row[2]))
            number+=1
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def delete_data(user_data, method):
    if method == 1:
        sql = '''DELETE FROM phonebook WHERE user_id = %s'''
    elif method == 2:
        sql = '''DELETE FROM phonebook WHERE user_phone = %s'''
    elif method == 3:
        sql = '''DELETE FROM phonebook WHERE user_name = %s'''
    elif method == 4:
        sql = '''DELETE FROM phonebook'''
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_data,))
        print('Удалено строк:', cur.rowcount)
        cur.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
