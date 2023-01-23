from fpdf import FPDF
import time
from datetime import date
import os
import tempfile

import sqlite3
connection = sqlite3.connect('inv.db')
cursor = connection.execute('SELECT COUNT(නම) FROM inv')
pagecount=int(cursor.fetchone()[0])
cursor = connection.execute('SELECT SUM(සමිල) FROM inv')
np=cursor.fetchone()[0]

cursor = connection.execute('SELECT SUM(අමිල) FROM inv')
ap=cursor.fetchone()[0]
print(pagecount)
print(np)
print(ap)
labe=int(np)-int(ap)
print(labe)
connection.commit()
connection.close()

y=int(pagecount)*10+97
print(y)

today = date.today()

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
current_time=str(current_time)
print(type(current_time))
d2 = today.strftime("%B %d, %Y")


pdf=FPDF('P','mm',(80,y))
pdf.set_auto_page_break(auto=1)
pdf.add_font('Iskoola Pota','',r'C:\Users\kezar\AppData\Local\Microsoft\Windows\Fonts\LJR~S17.TTF',uni=1)
pdf.add_page()
pdf.set_font('Iskoola Pota','',18)
pdf.cell(2,4,"    fk;au,a iqm¾",ln=1,)
pdf.cell(2,8,"       ud¾lÜ",ln=1)
pdf.set_font('Iskoola Pota','',12)
###########addres
pdf.cell(8,4,"ussa lKqj mdr y.a.,a, mdr t,a,lal, ",ln=1)
pdf.cell(2,4,"        0775143700",ln=1)
pdf.set_font('helvetica','',19)
pdf.cell(2,2,"-------------------------------------------------------------------------",ln=1,align='C')
pdf.set_font('helvetica','',9)
pdf.cell(4,4,'                                                                                                                                '+(current_time),align='C')
pdf.cell(12,4,'                                  '+(d2),align='R')
pdf.cell(29,4,'                                                                              ***WELCOME***',align='R',ln=1)
pdf.set_font('helvetica','',19)
pdf.cell(2,2,"-------------------------------------------------------------------------",ln=1,align='C')
pdf.add_font('sinhala','',r'C:\Users\kezar\AppData\Local\Microsoft\Windows\Fonts\iskpota_0.ttf',uni=1)
pdf.set_font('helvetica','',11)
pdf.cell(2,2,"                                                                          ",ln=1,align='C')
pdf.cell(2,2,'    NAME/Qnt',align='C',)
pdf.set_font('sinhala','',12)
pdf.cell(0,2,"              සාමාන්‍ය මිල          අප මිල",)
pdf.cell(2,4,"                                                                          ",ln=1,align='C')
pdf.set_font('helvetica','',19)
pdf.cell(2,2,"-------------------------------------------------------------------------",ln=1,align='C')


import sqlite3
connection = sqlite3.connect('inv.db')
cursor = connection.execute('select නම from inv')
cursor=cursor.fetchall()
samila = connection.execute('select ප්‍රමාණය from inv')
samila = samila.fetchall()
rsamila = connection.execute('select සමිල from inv')
rsamila = rsamila.fetchall()
amila = connection.execute('select අමිල from inv')
amila = amila.fetchall()

for name in cursor:

    x=str(name[0])
    print(x)
    pdf.set_font('sinhala', '', 12)
    pdf.cell(3,5,(x),ln=1 )
#################ස්මිල කියන්නෙ ප්‍රමානය
    for name in samila:
        y = str(name[0])
    print(y)
    pdf.set_font('helvetica', '', 11,)
    pdf.cell(1,4, (y),align='R')

    for name in rsamila:
        zz = str(name[0])
    print(zz)
    pdf.set_font('helvetica', '', 11)
    pdf.cell(1,4,'                     '+(zz),)

    for name in amila:
        zzz = str(name[0])
    print(zzz)
    pdf.set_font('helvetica', '', 11)
    pdf.cell(1,4,'                                               '+(zzz),ln=1)

pdf.set_font('helvetica','',19)
pdf.cell(2,12,"-------------------------------------------------------------------------",ln=1,align='C')
pdf.set_font('Iskoola Pota','',12)
pdf.cell(2,6,'    uq¨ jákdlu        '+str(np),ln=1)
pdf.cell(2,2,'    wfma us,           '+str(ap),ln=1)
pdf.set_font('Iskoola Pota','',12)

pdf.cell(0,6,'    ,o ,dnh           '+str(labe),ln=1)
pdf.set_font('helvetica', '',9 )
pdf.cell(1,2,'                                                    ',ln=1)
pdf.cell(1,0,'   ***GOOD DAY COME BACK***  ',ln=1)





pdf.output('1.pdf')


fd = os.startfile("1.pdf", "print")
