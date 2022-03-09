import os
import mysql.connector
from mysql.connector import Error
import pandas as pd
from dotenv import load_dotenv
load_dotenv()


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


connection = create_db_connection("localhost", "root", os.getenv("pw"), "test")
createDatabaseQuery = "CREATE DATABASE IF NOT EXISTS test"
execute_query(connection, createDatabaseQuery)
