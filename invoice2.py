import sqlite3
from datetime import date
from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3

connection = sqlite3.connect('inv.db')
cursor = connection.execute('select * from inv2')
cursor = cursor.fetchall()
print(cursor)
Total_QWpr=0.0
baseekata_danna_Q_WPR=0.0
MULUWIKUNUM=0.0
shudda_labaya=0.0

for name in cursor:
    x = str(name[0])
    connection = sqlite3.connect('item.db')
    cursor = connection.execute("SELECT QUNTY from item2 WHERE NAME='%s'" % x)
    wcursor = connection.execute("SELECT QUNTY from item2 WHERE NAME='%s'" % x)
    it = float(cursor.fetchone()[0])
    print(it)
    print(x)
    q = float(name[1])
    g = float(name[2])
    print(g)
    z = float(name[3])
    print(g)
    xy = float(name[4])
    print(g)
    b = float(q)
    print(q)

    connection.commit()
    cursor.close()
    itb = it - b
    print(itb)
    ################################################################
    b = q
    b = float(b)
    b = len(str(b))
    ###################laba alaba ekata####################################
    wcursor = connection.execute("SELECT WPRICE from item2 WHERE NAME='%s'" % x)
    WPR=float(wcursor.fetchone()[0])
    print("wikunum mila  "+str(WPR))
    print("pramne"+str(q))
    Q_WPR=q*WPR
    baseekata_danna_Q_WPR=baseekata_danna_Q_WPR+Q_WPR
    Total_QWpr=Total_QWpr+Q_WPR


print("mulu okkom wikunum PRIWARY mila*q = dalalabe" + str(Total_QWpr))
connection = sqlite3.connect('inv.db')
abcursor = connection.execute('SELECT SUM(qt) FROM inv3')
MULUWIKUNUM = abcursor.fetchone()[0]
shudda_labaya=MULUWIKUNUM-Total_QWpr
print(shudda_labaya)
print("meka"+str(baseekata_danna_Q_WPR))
###############################################################################################
def dine_iwarai():
    today = date.today()
    conn = sqlite3.connect('inv.db')
    c = conn.cursor()
    c.execute("INSERT INTO labaya VALUES ('%s','%s','%s')" % (today, MULUWIKUNUM, shudda_labaya))
    conn.commit()
    conn.close()


############################






#######################################################################








