import getpass
import cx_Oracle
from PyQt5.QtWidgets import QTableWidgetItem

from UI_ErrorDialog import UI_ErrorDialog

hostname = 'admlab2.cs.put.poznan.pl'
servicename = 'dblab02_students.cs.put.poznan.pl'
login = "INF141189"
pwd = "INF141189"

cnxn = None
cursor = None
outputlog = None

# Functions to operate on the database
def connect_with_database(is_check, inp_login, inp_password):
    global cnxn
    global cursor

    if not is_check:
        inp_login = login
        inp_password = pwd
    try:
        cnxn = cx_Oracle.connect(user=inp_login, password=inp_password, dsn='%s/%s' % (hostname, servicename))
    except cx_Oracle.DatabaseError as e:
        # Niepoprawna autoryzacja
        print(e)
        return False

    cursor = cnxn.cursor()

    # Poprawna autoryzacja
    return True

def load_table_structure(table, tablename):

    # Get columns
    sqlQuery = 'SELECT column_name FROM user_tab_cols WHERE table_name = \'{}\''.format(tablename)
    cursor.execute(sqlQuery)

    columns = []
    for item in cursor:
        columns.append(item[0])

    table.setColumnCount(len(columns))
    table.setHorizontalHeaderLabels(columns)

    load_table_data(table, tablename)

def load_table_data(table, tablename):
    # Get records
    sqlQuery = 'SELECT * FROM ' + tablename
    cursor.execute(sqlQuery)

    rows = []
    for item in cursor:
        rows.append(item)

    update_data_in_widget(table, tablename, rows)

def update_data_in_widget(table, tablename, rows):
    # Get columns
    sqlQuery = 'SELECT column_name FROM user_tab_cols WHERE table_name = \'{}\''.format(tablename)
    cursor.execute(sqlQuery)
    columns = []
    for item in cursor:
        columns.append(item[0])

    rowsCount = len(rows)
    table.setRowCount(rowsCount)
    for i in range(rowsCount):
        for j in range(len(columns)):
            table.setItem(i, j, QTableWidgetItem(str(rows[i][j])))

def apply_search(table, tablename, searchArg, searchArgValue):
    if (searchArgValue.text()==''):
        load_table_data(table, tablename)
        return

    sqlQuery = 'SELECT * FROM {} WHERE ({} LIKE \'%{}%\')'.format(tablename, searchArg, searchArgValue.text())
    try:
        cursor.execute(sqlQuery)
    except cx_Oracle.DatabaseError as e:
        #showErrorDialog('Condition', 'Uncorrect condition' )
        return

    rows = []
    for item in cursor:
        rows.append(item)

    update_data_in_widget(table, tablename, rows)

def apply_search_conditional(table, tablename, condition):
    if (condition == ''):
        load_table_data(table, tablename)
        return

    sqlQuery = 'SELECT * FROM {} WHERE ({})'.format(tablename, condition)
    try:
        cursor.execute(sqlQuery)
    except cx_Oracle.DatabaseError as e:
        print(e)
        showErrorDialog('Condition', 'Uncorrect condition\nExample: NAZWISKO=\'...\'')
        return

    rows = []
    for item in cursor:
        rows.append(item)
    update_data_in_widget(table, tablename, rows)

def showErrorDialog(type, name):
    errorDialog = UI_ErrorDialog(type, name)
    retValue = errorDialog.exec_()

# Into repository #
def insert_data(tablename, data):

    sqlQuery = 'INSERT INTO {} VALUES ({})'.format(tablename, data)
    try:
        cursor.execute(sqlQuery)
    except cx_Oracle.DatabaseError as e:
        print(e)
        showErrorDialog('Integrity violations', 'Incorrect data to insert')
        return
    outputlog.append('Inserted record: '+ data + ' in table: ' + tablename)

def update_data(tablename, data):
    sqlQuery = 'UPDATE {} {}'.format(tablename, data)
    try:
        cursor.execute(sqlQuery)
    except cx_Oracle.DatabaseError as e:
        print(e)
        showErrorDialog('Integrity violations', 'Unable to update this data')
        return
    outputlog.append('Updated data to: ' + data + ' in table: ' + tablename)

def remove_data(tablename, where):
    sqlQuery = 'DELETE FROM {} WHERE {}'.format(tablename, where)
    try:
        cursor.execute(sqlQuery)
    except cx_Oracle.DatabaseError as e:
        print(e)
        showErrorDialog('Integrity violations', 'Unable to delete this data')
        return
    outputlog.append('Removed data: ' + where + ' from table: ' + tablename)

def remove_all_data(tablename):
    sqlQuery = 'DELETE FROM {}'.format(tablename)
    try:
        cursor.execute(sqlQuery)
    except cx_Oracle.DatabaseError as e:
        print(e)
        showErrorDialog('Integrity violations', 'Unable to delete this data')
        return
    outputlog.append('Cleared table: ' + tablename)
