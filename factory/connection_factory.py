# -*- coding: utf-8 -*-

import MySQLdb

class ConnectionFactory(object):

    def get_connection(self):

        connection = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="",
            db="alura"
        )

        return connection
