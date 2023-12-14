#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Describes connection and sql queries to Postgres DB."""

from psycopg2 import OperationalError
from psycopg2.errors import UndefinedTable
import psycopg2


class BaseConnectionDB:
    """
    Describes connection to database.

    Kwargs accept all classic keywords arguments such is available in Postgres for user connection to DB.
    Creates connection instance during initialization if connection to DB will success. 

    Attributes:
    - conn: The database connection instance if connection established success, otherwise is string with error text.
    """

    conn = None

    def __init__(self, **kwargs):
        """
        Pass the connection values to the database you need.

        - *user* (str): The username for the database connection. Defaults to 'postgres'.
        - *password* (str): The password for the database connection. Defaults to 'root'.
        - *dbname* (str): The name of the database. Defaults to 'postgres'.
        - *host* (str): The host address of the database. Defaults to 'localhost'.
        - *port* (int): The port number for the database connection. Defaults to 5432.

        :param kwargs: connection parameters of the database.
        """
        self.user = kwargs.get('user', 'postgres')
        self.password = kwargs.get('password', 'root')
        self.dbname = kwargs.get('dbname', 'postgres')
        self.host = kwargs.get('host', 'localhost')
        self.port = kwargs.get('port', 5432)
        self.__connect()

    # Private method that trying to establish connection and set result in class attribute.
    def __connect(self):
        try:
            self.conn = psycopg2.connect(user=self.user, password=self.password,
                                         dbname=self.dbname, host=self.host, port=self.port)
        except (OperationalError, UnicodeDecodeError) as connection_error:
            self.conn = f'Проверьте данные подключения к БД (порт). Оригинальный текст ошибки: \n{connection_error}'
            if type(connection_error) is UnicodeDecodeError:
                self.conn = f'Проверьте данные подключения к БД. Неверные логин/пароль/хост.'

        return self.conn

    def execute_query(self, query):
        """
        Execute a SQL query and return the result set.

        :param query: (str) A pure SQL query.
        :return: Result set as a list of tuples.
                 In case of an undefined table (UndefinedTable exception),
                 the exception object is returned as an error.
        """
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
        """
        Print the connection parameters of the database.

        :return: None
        """
        print(self.dbname, self.host, self.port, self.user, self.password, sep='\n')


print(BaseConnectionDB(user='postgres').execute_query('SELECT * FROM mm.dept;'))
print(BaseConnectionDB.__doc__)
print(help(BaseConnectionDB.__init__))
