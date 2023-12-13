#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from psycopg2 import OperationalError
from psycopg2.errors import UndefinedTable
import psycopg2


class BaseConnectionDB:
    """ Describes connection to database. Kwargs accept all classic keywords arguments
     such is available in Postgres for user connection to DB.
     Creates connection instance during initialization if connection to DB will success. """
    def __init__(self, **kwargs):
        self.user = kwargs.get('user', 'postgres')
        self.password = kwargs.get('password', 'root')
        self.dbname = kwargs.get('dbname', 'postgres')
        self.host = kwargs.get('host', 'localhost')
        self.port = kwargs.get('port', 5432)
        self.conn = self.connection()

    # Establishes connection to DB if creds are valid and return connection object
    # otherwise return string with error text
    def connection(self):

        try:
            conn = psycopg2.connect(user=self.user, password=self.password,
                                    dbname=self.dbname, host=self.host, port=self.port)
        except (OperationalError, UnicodeDecodeError) as connection_error:
            conn = f'Проверьте данные подключения к БД (порт). Оригинальный текст ошибки: \n{connection_error}'
            if type(connection_error) is UnicodeDecodeError:
                conn = f'Проверьте данные подключения к БД. Неверные логин/пароль/хост.'

        return conn

    def execute_query(self, query):
        if type(self.conn) is str:
            return self.conn
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
        except UndefinedTable as err:
            return err
        queryset = cursor.fetchall()
        return queryset

    def connection_data(self):
        print(self.dbname, self.host, self.port, self.user, self.password)


# print(BaseConnectionDB(user='postgres').execute_query('SELECT * FROM mm.dept;'))
