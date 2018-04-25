import MySQLdb
from beautifultable import BeautifulTable
 
db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="masrestu",     # password
                     db="fuzzy")   # name of the database

# Membuat Objek untuk Execute SQL
sql = db.cursor()

table_umur = BeautifulTable()
table_masakerja = BeautifulTable()
table_gaji = BeautifulTable()

def _muda(umur):
    if umur <= 30:
        return 1
    if umur>=40:
        return 0
    if umur > 30 and umur < 40:
        return (40 - umur) / 10

def _parobaya(umur):
    if umur <= 35 or umur >= 50:
        return 0
    if umur > 35 and umur < 45:
        return (umur - 35)/ 10
    if umur > 45 and umur < 50:
        return (50 - umur) / 5
def _tua(umur):
    if umur <= 40:
        return 0
    if umur>=50:
        return 1
    if umur > 40 and umur < 50:
        return (umur - 40) / 10

def predict_Umur(umur):
    muda = _muda(umur)
    parobaya = _parobaya(umur)
    tua = _tua(umur)

    return muda, parobaya, tua


def _baru(masakerja):
    if masakerja <= 5:
        return 1
    if masakerja >= 15:
        return 0
    if masakerja > 5 or masakerja < 15:
        return (15 - masakerja)/10


def _lama(masakerja):
    if masakerja <= 10:
        return 0
    if masakerja >= 25:
        return 1
    if masakerja > 10 or masakerja < 25:
        return (masakerja - 10)/15

def predict_MasaKerja(masakerja):
    baru = _baru(masakerja)
    lama = _lama(masakerja)
    return baru, lama

def _rendah(gaji):
    if gaji <= 300000:
        return 1
    if gaji >=800000:
        return 0
    if gaji > 300000 or gaji < 800000:
        return (800000 - gaji) / 500000

def _sedang(gaji):
    if gaji <= 500000 or gaji >= 1500000:
        return 0
    if gaji> 500000 and gaji < 1000000:
        return (gaji - 500000)/ 500000
    if gaji > 1000000 and gaji < 1500000:
        return (1500000 - gaji) / 500000
 
def _tinggi(gaji):
    if gaji <= 1000000:
        return 0
    if gaji>=2000000:
        return 1
    if gaji > 1000000 or gaji < 2000000:
        return (gaji - 1000000) / 1000000

def predict_Gaji(gaji):       
    rendah = _rendah(gaji)
    sedang = _sedang(gaji)
    tinggi = _tinggi(gaji)
    return rendah, sedang, tinggi


sql.execute("SELECT * FROM karyawan")

header_umur = ["No","Nama","Umur","Muda","Parobaya","Tua"]
header_masakerja = ["No","Nama","Masa Kerja","Baru","Lama"]
header_gaji = ["No","Nama","Gaji","Rendah","Sedang","Tinggi"]

table_umur.column_headers = header_umur
table_masakerja.column_headers = header_masakerja
table_gaji.column_headers = header_gaji

for row in sql.fetchall() :
    muda, parobaya, tua = predict_Umur(row[2])
    #print(row[0], " ", row[1], " ", row[2], " ", row[3], " ", row[4], " ", muda, " ", parobaya, " ", tua)
    table_umur.append_row([row[0], row[1], row[2], muda, parobaya, tua])

    baru, lama = predict_MasaKerja(row[3])
    table_masakerja.append_row([row[0], row[1], row[3], baru, lama])

    rendah, sedang, tinggi = predict_Gaji(row[4])
    table_gaji.append_row([row[0], row[1], row[4], rendah, sedang, tinggi])




print(table_umur)
print(table_masakerja)
print(table_gaji)