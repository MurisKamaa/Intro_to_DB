#!/usr/bin/env python3
"""
MySQLServer.py
Script to create the database alx_book_store in MySQL.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update host/user/password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="channel540",
            database="alx_book_store"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection safely
        try:
            if cursor:
                cursor.close()
            if connection.is_connected():
                connection.close()
        except:
            pass

if __name__ == "__main__":
    create_database()
