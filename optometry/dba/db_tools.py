# -*- coding=utf-8 -*-
import pymysql.cursors


def get_connection(env):
    host = env['host']
    user = env['user']
    password = env['password']
    db = env['db']

    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 db=db,
                                 charset="utf8",
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


def commit_db(connection, sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
    connection.commit()


def select_db_one(connection, sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchone()
        return result


def select_db_all(connection, sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results


if __name__ == '__main__':
    DB_ENV = {
        'host': '192.68.75.25',
        'user': 'seeing',
        'password': 'seeing',
        'db': 'seeing',
    }
    print get_connection(DB_ENV)
