#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Describes connection and sql queries to Postgres DB."""

from django.utils.translation import gettext as _
from psycopg2 import OperationalError
from psycopg2.errors import UndefinedTable, SyntaxError
import psycopg2
# from hospital_pg import sql_queries


class BaseConnectionDB:
    """
    Describes connection to database.

    Kwargs accept all classic keywords arguments such is available in Postgres for user connection to DB.
    Creates connection instance during initialization if connection to DB will success with given creds. 

    Attributes:
    - conn: The database connection instance if connection established success, otherwise is string with error text.
    """

    conn = None
    cursor = None

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
            self.cursor = self.conn.cursor()
        except (OperationalError, UnicodeDecodeError) as connection_error:
            self.conn = f'Проверьте данные подключения к БД (порт). Оригинальный текст ошибки: \n{connection_error}'
            if type(connection_error) is UnicodeDecodeError:
                self.conn = f'Проверьте данные подключения к БД. Неверные логин/пароль/хост.'
        return self.conn
    
    def _get_columns_list(self):
        if type(self.conn) is str:
            return 'Class method get_column_names() can\'t be used with string object.'
        result = self.check_query(self.cursor, "SELECT column_name FROM information_schema.columns WHERE table_schema = 'mm' AND table_name = 'dept';")
        self.__close_connection
        result = [column[0] for column in result]
        return result

    def __close_connection(self):
        if type(self.conn) is str:
            return
        self.cursor.close()
        self.conn.close()

    def check_query(self, cursor, query):
        """
        Helper method to execute a SQL query and handle errors.

        :param cursor: Database cursor.
        :param query: (str) A pure SQL query.
        :return: (list) Result set as a list of tuples or the exception object.
        """
        try:
            cursor.execute(query)
        except (UndefinedTable, SyntaxError) as err:
            return err
        return cursor.fetchall()

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
        result = self.check_query(self.cursor, query)
        self.__close_connection
        return result

    def get_connection_data(self): 
        """
        Print the connection parameters of the database.

        :return: (dict) Dictionary containing database connection parameters.
        """
        return {
            'dbname': self.dbname,
            'host': self.host,
            'port': self.port,
            'user': self.user,
            'password': self.password
        }


# print(BaseConnectionDB().execute_query('SELECT * FROM mm.dept;'))
# print(BaseConnectionDB()._get_columns_list())

