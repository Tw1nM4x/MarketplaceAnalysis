import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('database_footbot.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS user ('
                 'id PRIMARY KEY,'
                 'name_user TEXT (50),'
                 'name_club   TEXT (50),'
                 'emblem      TEXT (8),'
                 'income      INTEGER,'
                 'money       INTEGER,'
                 'fans        INTEGER,'
                 'id_squad    INTEGER,'
                 'id_match    INTEGER,'
                 'quiz    INTEGER'
                 ');')

    base.commit()



