# *Сделать связь таблиц

import os
import sqlite3
from sqlite3 import Error
import hw_01
import hw_02

FILE_BD = "My_BD"

def create_connection(path):
  connection = None

  try:
    connection = sqlite3.connect(path)
    print('Connection')
  except Error as err:
    print(err)

  return connection

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(err)


def execute_query(connection, query):
  cursor = connection.cursor()

  try:
    cursor.execute(query)
    connection.commit()
  except Error as err:
    print(err)

the_way = os.getcwd()
path = os.path.join(the_way, FILE_BD)
connection = create_connection(path)

execute_query(connection, hw_01.create_students_table)
execute_query(connection, hw_01.create_students)
execute_query(connection, hw_02.creat_audit_table)
execute_query(connection, hw_02.creat_audit)

studentiki = execute_read_query(connection, hw_01.select_students)


cursor = connection.cursor()

#выбираю по значения предмета, в какую аудиторию определен студент

cursor.execute('''
    SELECT DISTINCT
        surname,
        number
    FROM
        students,
        audit
    WHERE audit.subject = students.subject
    ''')

result = cursor.fetchall()
for item in result:
    print(item)